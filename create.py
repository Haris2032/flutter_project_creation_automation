import sys
import os
from github import Github

username = "" #Insert your github username here
password = "" #Insert your github password here

def create():
    folderName = str(sys.argv[1])
    os.system("cd ###Your required path### && flutter create {}".format(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
