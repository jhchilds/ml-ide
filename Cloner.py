import requests
import os
import csv
from github import Github

# Github Repo Cloner
class Cloner:
    def __init__(self, num_repos):
        self.langs = ['python', 'c++', 'c', 'javascript', 'java', 'php', 'swift', 'ruby', 'c#', 'r', 'matlab', 'vb.net']


    def clone_repos(self):
        print("Cloning repos...")
        print("...")
        for lang in self.langs:
            with open(lang + '_repos.csv', newline='') as csvfile:
                r = csv.reader(csvfile, delimiter=',')
                for row in r:
                    row_f = ', '.join(row)
                    os.system("git clone git@github.com:" + row_f)

    # Github has an endpoint URL that returns
    # public repo metadata in groupings of 100
    def accumulate_repos(self):
        test = ['java']
        g = Github("jhchilds", "Ad141700!@#$%")

        for lang in test:
            repositories = g.search_repositories(query='language:' + lang)
            with open('data/'+ lang + '_repos.csv', 'w', newline='') as csvfile:
                w = csv.writer(csvfile, delimiter=',')
                for repo in repositories:
                    w.writerow([repo.full_name])




