#!/bin/bash

#script to clone all repos from a project on bitbucket
#provide your username as an arg
# this script is messy, two out put files and a bunch of repos cloned in your current dir

#initial clean up
if [[ -fe projecturl.txt  || -fe repourl.txt ]]
then

    rm projecturl.txt && rm repourl.txt
fi
curl -u ${1}  "http://gitlaburl/rest/api/1.0/projects/" | jq -r  '.values[].key'  > projectkey.txt
curl -u ${1}  "http://gitlaburl/rest/api/1.0/projects/" | jq -r  '.values[].name'  > projectname.txt
url="http://gitlaburl/rest/api/1.0/projects"
for projectkey in $(cat projectkey.txt)
 do

   echo "$url/$projectkey/repos" >> projecturl.txt
 #declare -a repos= $(curl -u ${1} http://gitlaburl/rest/api/1.0/projects/${projectname} | jq -r '.links.self[].href')
done

for projecturl in $(cat projecturl.txt)
 do
  curl -u ${1} $projecturl | jq -r '.values[].links.clone[].href' >> repourl.txt
  sed -i '' '/^ssh/d' repourl.txt

done


  for repo in $(cat repourl.txt)
    do
    git clone $repo

done
