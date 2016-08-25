#!/bin/bash
#go through each repository and do the thing

cd repos/
for repo in $(ls -d *);
 do
 cd /PATH/TO/REPOS/$repo && echo "I'm in "$repo
 git remote rename origin bitbucket
 git remote add origin https://github.com/eltorocorp/$repo.git
 git push origin master

done
