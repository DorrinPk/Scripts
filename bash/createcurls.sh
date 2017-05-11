#!/bin/bash
# This script is made to set up my API calls ready for me
# I originally made this because I can't have dynamic vars in JSON
# yeah I could have wrote this in something else
# don't judge me ^_^
# this is ran after my clonerepos.sh script

jsonhead="curl -u "\""USER:PASS"\"" https://api.github.com/orgs/REPONAME/repos -d "\'"{"\""name"\"":"\"""
jsontail=""\"","\""private"\"":""\""true""\""}"\'""
echo "#!/bin/bash" >> runcurls.sh
echo '\n' >> runcurls.sh
for name in $(cat newreponame.txt)
 do
   echo $jsonhead$name$jsontail >> runcurls.sh

 done
