import requests
import json

message = ""
start_slack_message_block = '[{"type":"header","text": {"type":"plain_text","text":"%s"}},'
divider_slack_message_block = '{"type": "divider"},'
project_slack_message_block = '{"type":"section","text":{"type":"mrkdwn","text":"%s"}},'

git_api_path = "https://api.github.com/"
slack_api_send_message = "https://slack.com/api/chat.postMessage"

users_info = [
{'gh':'git_user','slack':'slack_member_ID'},
]
prs = {}

slack_bot_token = "xoxb-...."

github_requests = requests.Session()
github_requests.auth = ('git_user','git_access_token')
slack_requests = requests.Session()

# prendi le pr delle repo per utente
for user in users_info:
	json_repos = github_requests.get(git_api_path + "users/" + user['gh'] + "/subscriptions").json()
	message = start_slack_message_block % ("Hello " + user['gh'] + "! \n Here's the list of open PRs to check! ")
	for repo in json_repos:
		if(repo['owner']['login'] == "everli"):
			if (not (repo['name'] in prs)):
				json_prs = github_requests.get(git_api_path + "repos/everli/" + repo['name'] + "/pulls?state=open").json()
				prs[repo['name']] = "*List of pending PRs on <https://github.com/everli/" + repo['name'] + "/pulls|" + repo['name'] + "> project:* \n"
				for pr in json_prs:
					prs[repo['name']] += "*<" + pr['html_url'] + "|#" + str(pr['number']) + " - " + pr['title'] + ">* \n"
			message += divider_slack_message_block + project_slack_message_block % (prs[repo['name']])
	#curl slack
	slack_data={'token':slack_bot_token,
				'channel':user['slack'],
				'text':"New PRs to check!",
				'blocks': message + "]",
				'as_user': True}
	slack_requests.post(url = slack_api_send_message, data = slack_data)
