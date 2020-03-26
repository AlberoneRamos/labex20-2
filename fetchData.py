import requests
import json
import sys
import errno
import time

headers = {'Authorization': 'Bearer {}'.format(sys.argv[1])}


def runQuery(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
      raise Exception('Error {}. {}'.format(request.status_code, query))


query = '''
{
  user(login: "gvanrossum") {
    repositories(first: 50) {
      nodes {
        name
        primaryLanguage {
          name
        },
        stargazers {
          totalCount
        },
        watchers {
          totalCount
        },
        createdAt,
        forks {
          totalCount
        },
        url,
        isFork
      }
    }
  }
}
'''

filename = 'output.json'
nodes = runQuery(query)['data']['user']['repositories']['nodes']
print(nodes)
with open('output.json', 'w') as file:
  json.dump([node for node in nodes if node['primaryLanguage'] is not None and node['primaryLanguage']['name'] == 'Python' and node['isFork'] != True], file)

print('Written to file output.json')