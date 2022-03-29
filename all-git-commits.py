#!/usr/bin/python
# **************************************************
# Usage (how to execute the script)
# python3 ./all-git-commits.py -u <Git> -d <directory> -r <repo> -n <number of commits>
# **************************************************

# Note for Noah and Ali - copy this command into the terminal and press enter.
# The files will all start downloading:
# -------------------------------------------------
#     python3 ./all-git-commits.py -u LaurierCS -d Pod1RepoTest -r Pod1



import getopt
import json
import os
import shutil
import subprocess
import sys

# from urllib2 import urlopen
from urllib.request import urlopen

def Usage():
  print("Usage$ %s -u <github username> -d <directory name to save downloaded files> -r <repo to download> -n <number of commits>" % sys.argv[0])
  print("  -u <github user>  github user name")
  print("  -d <directory>    local directory for repos commits")
  print("  -r <repo>         specific repo")
  print("  -n <number>       (optional) number of commits (newest to oldest)")
  print("  -l <listonly>     (optional) list only, no checkout")

def main():

  githubUser  = ''
  destDirectory = ''
  currentRepo = ''
  numberCommits = 10000000
  listOnly = False
  
  try:
    # process command arguments
    ouropts, args = getopt.getopt(sys.argv[1:],"u:d:r:n:lh")
    for o, a in ouropts:
      if   o == '-u':
        githubUser = a
      if   o == '-d':
        destDirectory = a
      if   o == '-r':
        currentRepo = a
      if   o == '-n':
        numberCommits = int(a)
      if   o == '-l':
        listOnly = True
      elif o == '-h':
        Usage()
        sys.exit(0)
  except getopt.GetoptError as e:
    print(str(e))
    Usage()
    sys.exit(2)

  if type(githubUser) != str or len(githubUser) <= 0:
      print("please use -u for github user")
      Usage()
      sys.exit(0)
  if type(destDirectory) != str or len(destDirectory) <= 0:
      print("please use -d for local directory")
      Usage()
      sys.exit(0)
  if type(currentRepo) != str or len(currentRepo) <= 0:
      print("please use -r for repo")
      Usage()
      sys.exit(0)

  commitsLink = "https://api.github.com/repos/{0}/{1}/commits".format(githubUser, currentRepo)
  f = urlopen(commitsLink)
  commits = json.loads(f.readline())
  print("repo: '{0}' ; total commits: {1}".format(currentRepo, len(commits)))

  os.mkdir(destDirectory)
  os.chdir(destDirectory)

  repoLink = "https://github.com/{0}/{1}.git".format(githubUser, currentRepo)
  print(repoLink)
  count = 0
  for commit in commits:
    d = commit['commit']['committer']['date']
    name = commit['commit']['committer']['name']
    sha = commit['sha']
    subdir = "{0}-{1}-{2}-{3}".format(currentRepo, d, name, sha)
    print(subdir)
    if not listOnly:
      subprocess.call(['git', 'clone', repoLink, subdir])
      os.chdir(subdir)
      subprocess.call(['git', 'checkout', sha])
      os.chdir(os.path.join('..'))

    # are we done?
    count += 1
    if (count >= numberCommits):
      break


if __name__ == "__main__":
  main()