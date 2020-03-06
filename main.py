from Cloner import Cloner
from github import Github
from github.Rate import Rate
import csv
def main():
    # g = Github("jhchilds", "Ad141700!@#$%")

    cloner = Cloner(1000)
    cloner.accumulate_repos()
    # cloner.clone_repos()



    # print(g.get_rate_limit())

main()

