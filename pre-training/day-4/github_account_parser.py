# Use the GitHub public API (no auth needed) to fetch any user's profile.
# Print: username, bio, public repos count, followers, top 5 repos by stars (name + star count +
# language).
# Handle: user not found (404), rate limit hit (403), network error. Each with a useful error
# message.
# Bonus: let the user pass the GitHub username as a command line argument (sys.argv).

import requests
import sys

def get_github_profile(username):
	user_url = f'https://api.github.com/users/{username}'
	response = requests.get(user_url)
	if response.status_code == 404:
		print(f'User {username} not found')
		return
	if response.status_code == 403:
		print(f'Rate limit hit for user {username}')
		return
	if response.status_code == 200:
		repos_url = f'https://api.github.com/users/{username}/repos'
		repos_response = requests.get(repos_url)

		data = response.json()
		print(f'Username: {data["login"]}')
		print(f'Bio: {data["bio"]}')
		print(f'Public repos: {data["public_repos"]}')
		print(f'Followers: {data["followers"]}')

		print('---------------------------	')
		repos = repos_response.json()
		repos.sort(key=lambda x: x['stargazers_count'], reverse=True)
		top_5_repos = repos[:5]
		for repo in top_5_repos:
			print(f'{repo["name"]} - {repo["stargazers_count"]} - {repo["language"]}')
		print('---------------------------	')
	return

if __name__ == '__main__':
	username = sys.argv[1]
	get_github_profile(username)