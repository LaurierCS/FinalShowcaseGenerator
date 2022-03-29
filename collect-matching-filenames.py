from pathlib import Path
# Glob pattern tester tool (to help test patterns to look for)
# https://www.digitalocean.com/community/tools/glob?comments=true&glob=%2Ftemplates%2F%2A%2A%2F%2A%2B%28.js%7C.html%29&matches=false&tests=%2F%2F%20These%20will%20all%20match%20as%20the%20globstar%20matches%20zero%20or%20more%20directories%20recursively&tests=%2Ftemplates%2Fcrud%2Fbast.html&tests=%2Ftemplates%2Fbast.html&tests=%2Fcrud%2Fbast.html&tests=%2Ffile.js&tests=%2Fone%2Ffile.js&tests=%2Fone%2Ftwo%2Ffile.js&tests=%2Fone%2Ftwo%2Fthree%2Ffile.js

# ****************************************
# This script is for after downloading the repo commits
# Command to run script:
#   python3 collect-matching-filenames.py
# ****************************************


# for path in Path('Pod1RepoTest').rglob('*.txt'):
#     print("Path: ", path.name, path)

#The files we want to search for and collect
file_patterns = [
    "manage.py",
    "views.py",
    "forms.py",
    "urls.py",
    "templates/**/*.html", #Finds all html files in the templates folder
    # "templates/base.html", #Finds all html files in the templates folder

    "static/**/*+(.css|.js)", #Finds all js and css files in the static files folder
]

# for path in Path('Pod1RepoTest').rglob('templates/**/*.html'):
#     print("Path: ", path.name, path)
file_paths = {}
for pattern in file_patterns:
    print("PATTERN: ", pattern)
    if pattern not in file_paths.keys():
        file_paths[pattern] = Path('Pod1RepoTest').rglob(pattern)
    
    print(f"Paths for {pattern}: ", file_paths[pattern])
    # for path in file_paths[pattern]:
    #     print("Path: ", path.name, path)


# os.mkdir(path)
# print("Directory '% s' created" % directory)

# for key, value in file_paths.items():
#     os.mkdir(path)

# print("Directory '% s' created" % directory)