import os
import json
import pygount

with open('output.json', 'r') as file:
  data = json.load(file)

def getLinesOfCode(repo):
  os.system(f'git clone {repo["url"]} {repo["name"]}')
  loc = os.popen(f'cd {repo["name"]} && git ls-files | grep .py | xargs cat | wc -l').read()
  os.system(f'rm -rf {repo["name"]}')
  
  if len(loc) > 0:
    return int(loc[0:-1])
  else:
    return int(0)

print([getLinesOfCode(repo) for repo in data])
