#!/bin/bash
# sudo apt-get install jq
# e anche gh!

base_path="$HOME/Projects"
declare -A messages
bot_token="xoxb-3129647379621-3156303839808-xqVKWGaB41XKGa3IEGsPU0hT"


execute_user(){
	echo $1
	echo $2
	echo $3
	IFS=',' read -ra prjs <<< "$3"
	# $3 dovrebbe essere un array, adatta a ciclo!
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
		echo $message
		$(curl -X POST "https://slack.com/api/chat.postMessage" -H "accept: application/json" -d token=$bot_token -d channel=$2 -d text="$message" -d as_user=true)
	done
}

execute_user andrea U033WGGV459 leia,c-3po,lando-v2
execute_user alex U033WGGV459 leia,c-3po,lando-v2
#for str in ${projects[@]}; do

#done

#$(curl -X POST "https://slack.com/api/chat.postMessage" -H "accept: application/json" -d token=$bot_token -d channel=$number_id -d text="Hello" -d as_user=true)
