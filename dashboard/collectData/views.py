from github import Github

class collect_data_organization:

    def __init__(self, user_name, password):
        self.git = Github(user_name, password) # Use token ?

    def collect_data_from_organization(self, org_name):
        org = self.git.get_organization(org_name)
        repos = org.get_repos()

        org_commits = 0
        org_prs = 0
        org_closed_issues = 0
        repositories = []
        contributors = []
        for repo in repos:
            # Organization info
            org_commits += repo.get_commits().totalCount
            org_prs += repo.get_pulls().totalCount
            org_closed_issues += repo.get_issues(state='closed').totalCount

            #repositories
            repositories.append(
                {
                    'name': repo.full_name,
                    'commits': repo.get_commits().totalCount,
                    'closed_issues': repo.get_issues(state='closed').totalCount
                }
            )

            #contributors
            org_contributors = repo.get_contributors()
            for contrib in org_contributors:
                contributors.append(
                    {
                        'name': contrib.name
                    }
                )

        dict = {
            'commit': org_commits,
            'prs': org_prs,
            'collab': org.collaborators,
            'closed_issues': org_closed_issues,
            'repositories': repositories,
            'contributors': contributors
        }

        print(dict)


