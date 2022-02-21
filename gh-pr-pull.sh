#!/bin/bash
# install jq and gh

# insert your own base path
base_path="$HOME/Projects"
declare -A messages
bot_token="xoxb-3129647379621-3156303839808-xqVKWGaB41XKGa3IEGsPU0hT"


execute_user(){
	IFS=',' read -ra prjs <<< "$3"
	for prj in ${prjs[@]}; do
		cd "$base_path/$prj"
		r=$(gh pr list --json url)
		message="*List of pending PRs on <https://github.com/everli/$prj/pulls|$prj> project:*
		"
		urls=$(jq -rc '.[].url' <<< "${r[@]}");
		for url in $urls; do
			message+="-$url
		"
		done
		$(curl -X POST "https://slack.com/api/chat.postMessage" -H "accept: application/json" -d token=$bot_token -d channel=$2 -d text="$message" -d as_user=true)
	done
}

# $1 username
# $2 user slack_id
# $3 projects comma separated string
execute_user andrea U033WGGV459 leia,c-3po,lando-v2

