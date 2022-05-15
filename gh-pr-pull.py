import requests
import json
from config import users_info

message = ""
start_slack_message_block = '[{"type":"header","text": {"type":"plain_text","text":"%s"}},'
divider_slack_message_block = '{"type": "divider"},'
project_slack_message_block = '{"type":"section","text":{"type":"mrkdwn","text":"%s"}},'

git_api_path = "https://api.github.com/"
slack_api_send_message = "https://slack.com/api/chat.postMessage"

prs = {}

slack_bot_token = "xoxb-...."

github_requests = requests.Session()
github_requests.auth = ('git_user','git_access_token')
slack_requests = requests.Session()

def getFilters(repo_filters, repo_name):
	return '%20'.join(repo_filters) + "%20repo:everli/" + repo_name

for user in users_info:
	message = start_slack_message_block % ("Hello " + user['gh'] + "! \n Here's the list of open PRs to check! ")
	for repo in user['projects']:
		filters = getFilters(user['projects'][repo]['filters'], repo)
		json_prs = github_requests.get(git_api_path + "search/issues?q=" + filters).json()
		prs = "*List of pending PRs on <https://github.com/everli/" + repo + "/pulls|" + repo + "> project:* \n"
		prs += "_{filter used: " + requests.utils.unquote(filters) + "}_\n"
		for pr in json_prs['items']:
			prs += "*<" + pr['html_url'] + "|#" + str(pr['number']) + " - " + pr['title'] + ">* \n"
		message += divider_slack_message_block + project_slack_message_block % (prs)
	
	#curl slack
	slack_data={'token':slack_bot_token,
				'channel':user['slack'],
				'text':"New PRs to check!",
				'blocks': message + "]",
				'as_user': True}
	slack_requests.post(url = slack_api_send_message, data = slack_data)
	