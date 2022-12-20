from git import Repo
import subprocess
import sys
import os

repo = Repo('/home/nutanix/dummy_project1')
repo.index.add(['/home/nutanix/dummy_project1/test.py'])
repo.index.commit('1st commit')
origin = repo.remote(name='origin')
origin.push()
print("push success!")
