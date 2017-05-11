import boto3
from collections import defaultdict
import json

instances=[i for i in boto3.resource('ec2', region_name='us-east-1').instances.all()]
ec2 = boto3.resource('ec2')

running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

ec2info = defaultdict()

for i in instances:
 if 'Monitor' in [t['Key'] for t in i.tags]:

    for instance in running_instances:
        for tag in instance.tags:
  	  if 'Name'in tag['Key']:
            name = tag['Value']
            #add instance info to dictionary
	    ec2info[instance.id] = {
        	'Name': name,
         	'Private IP': instance.private_ip_address,
         	}

Name=['Name']
PrivateIP=['Private IP']
Service=['PING','Check Users','CPU load','Check SSH','Total Process', 'Disk Space']
Command=['check_ping!100.0,20%!500.0,60%', 'check_nrpe!check_users', 'check_nrpe!check_load','check_ssh', 'check_nrpe!check_total_procs', 'check_nrpe!check_disk_space' ]

for instance_id, instance in ec2info.items():
    for namekey, ipkey in zip(Name, PrivateIP):
        configfile=open(str(instance[namekey]) + ".cfg", 'w')
        configfile.write("define host { \n")
        configfile.write("	use			 linux-server \n")
        configfile.write("	host_name	         " + instance[namekey]+ " \n")
	configfile.write("	alias		         " +   instance[namekey]+ " \n")
        configfile.write("        address                " + instance[ipkey]+" \n")
        configfile.write("        register                 1 \n")
        configfile.write(" 	hostgroups               AWS_hosts \n")
        configfile.write("	contact_groups           admins \n")
        configfile.write("} \n\n")

    for service, cmd in zip(Service, Command):
        configfile.write("define service { \n")
        configfile.write("	host_name		  " +   instance[namekey]+ " \n")
        configfile.write("	service_description       " +   service + " \n")
	    configfile.write("	check_command		  " +   cmd + " \n")
    	configfile.write("	max_check_attempts	  2 \n")
    	configfile.write("	check_interval		  2 \n")
    	configfile.write("	retry_interval		  2 \n")
    	configfile.write("	check_period		  24x7 \n")
    	configfile.write("	check_freshness	          1 \n")
    	configfile.write("	contact_groups		  admins \n")
    	configfile.write("	notification_interval	  2 \n")
    	configfile.write("	notification_period	  24x7 \n")
    	configfile.write("	notifications_enabled	  1 \n")
    	configfile.write("	register		  1 \n")
      	configfile.write("} \n\n")

configfile.close()

