import os
import json

with open('output.json', 'r') as file:
  data = json.load(file)

def getLinesOfCode(repo):
  print(f"Cloning {repo['name']}")
  os.system(f'git clone --quiet {repo["url"]} {repo["name"]}')
  loc = os.popen(f'cd {repo["name"]} && git ls-files | grep .py | xargs cat | wc -l').read()
  os.system(f'rm -rf {repo["name"]}')
  print(f"{repo['name']} has {loc[0: -1]} lines of code.")

  if len(loc) > 0:
    return int(loc[0:-1])
  else:
    return int(0)


with open('linesOfCode.json', 'w') as file:
  json.dump([dict(repo, **{"linesOfCode": getLinesOfCode(repo)}) for repo in data], file)
