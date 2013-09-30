from subprocess import call
from utils import Utils
import os

os.chdir(Utils().WORKSPACE_DIR)
f = open('doc/repos.txt', 'r')
for repo in f:
    call(["git", "clone", repo.strip()])
