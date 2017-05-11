require 'octokit'

client = Octokit::Client.new(:access_token => "<token>", auto_traversal: true, per_page:500)


user = client.user
user.login

client.org_repos('<org>', {:type => 'all'}).each do |repo|
    puts repo.name
    client.add_team_repository(<team id>,"<org>/"+repo.name, {:permission => 'push'})

end    
