from pathlib import Path

for path in Path('Pod1RepoTest').rglob('*.txt'):
    print("Path: ", path.name)