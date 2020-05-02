import requests
import os
import csv
from github import Github


# Github Repo Cloner
class Cloner:
    def __init__(self):
        self.langs = ['haskell']

    def clone_repos(self):
        print("Cloning repos...")
        print("...")
        for lang in self.langs:
            with open('../repos/' + lang + '_repos.csv', newline='') as csvfile:
                r = csv.reader(csvfile, delimiter=',')
                limit = 10
                for row in r:
                    row_f = ', '.join(row)
                    os.system(f"git clone https://github.com/{row_f} ../repos-cloned/{row_f.split('/')[-1]}")
                    if limit <= 0:
                        return
                    limit -= 1

    # Github has an endpoint URL that returns
    # public repo metadata in groupings of 100
    def accumulate_repos(self):
        langs = ['haskell']
        f = open("pw.txt", "r")
        username = f.readline().rstrip()
        pw = f.readline().rstrip()

        g = Github(username, pw)
        print(g.get_rate_limit())

        for lang in langs:
            repositories = g.search_repositories(query='language:' + lang)
            with open('../repos/'+ lang + '_repos.csv', 'w', newline='') as csvfile:
                w = csv.writer(csvfile, delimiter=',')
                for repo in repositories:
                    w.writerow([repo.full_name])




