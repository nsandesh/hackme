import requests

def get_pr_files(owner, repo, pull_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve PR files. Status code: {response.status_code}")
        return None

def get_line_numbers(owner, repo, pull_number):
    pr_files = get_pr_files(owner, repo, pull_number)

    if pr_files:
        for pr_file in pr_files:
            filename = pr_file["filename"]
            additions = pr_file["additions"]
            deletions = pr_file["deletions"]
            changes = pr_file["changes"]

            print(f"File: {filename}, Additions: {additions}, Deletions: {deletions}, Changes: {changes}")

            # If you want to get the specific lines changed, you can use the GitHub API's
            # 'GET /repos/:owner/:repo/pulls/:pull_number/files/:file_sha' endpoint.

if __name__ == "__main__":
    owner = "your_username"
    repo = "your_repository"
    pull_number = 1  # Replace with your actual pull request number

    get_line_numbers(owner, repo, pull_number)
