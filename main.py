from Cloner import Cloner
from github import Github
from github.Rate import Rate
import csv
def main():

    cloner = Cloner()
    cloner.accumulate_repos()
    # cloner.clone_repos()


main()

