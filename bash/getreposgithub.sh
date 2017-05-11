#handy github things 

curl -u "<USER>" https://api.github.com/orgs/<ORG>/repos | grep -o 'git@[^"]*'
curl -u "<USER>" https://api.github.com/orgs/<ORG>/repos | jq '.[] | .ssh_url'
curl -u "<USER>" https://api.github.com/orgs/<ORG>/repos?per_page=500 | jq '.[] | .ssh_url'
