# gh-pr-pull
Shell/Python script to pull GitHub PRs of specific projects and to list them in Slack

# Python ver Set-up
What do we need to start using this script?

- A Slack bot active in the channel we wish to send the PRs
- The token for the said bot
- A GitHub account active in the organization you wish to fetch PRs from
- A GitHub access token from said account. *The token must have permission to read pull requests*

Now for the actual set-up
- Set the variable "slack_bot_token" with the slack token
- Set the first variable of "github_request.auth" with the name of the GitHub account active in the organization
- Set the second variable of "github_request.auth" with an access token from the GitHub account active in the organization

We are almost done, one last thing to set-up

The variable users_info is an array of the users we want to notify through this script:

- For each user insert their GitHub username in the "gh" key and their slack member id in the "slack" key

# How do I get the slack member id of a user?
- Open a conversation with a user
- Click their name at the top of the conversation
- In the popup that opens click "View full profile"
- In the new window click "More"
- At the bottom of the menu you'll find "Copy member ID"
- Click on it to copy it to your clipboard!
