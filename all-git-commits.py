#!/usr/bin/python

# python3 ./all-git-commits.py -u <user> -d <directory> -r <repo> -n <number of commits>
#
# Tool to inspect Github and pull local copies of all commits for
# for the given user.
#
# Why?  Every ask yourself the question 'I know I did this before, but
#       which repos commit was it in?'
# With all files local, you can use any serach-in-files app to look.
#
# Companion App: all-gethub.py to get all repos for a user.

import getopt
import json
import os
import shutil
import subprocess
import sys

from urllib2 import urlopen

def Usage():
  print("Usage$ %s -u <your github username to download from> -d <directory where you want to save the downloaded repo> -r <the Github repo to download> -n <number of commits to download>" % sys.argv[0])
  print("  -u <github user>  your github user name that you want to get the repos from ")
  print("  -d <directory>    where you want save the downloaded repos (aka commits) from github")
  print("  -r <repo>         which Github repo to download all the commits from ")
  print("  -n <number>       (optional) number of commits you want to download (newest to oldest)")
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
