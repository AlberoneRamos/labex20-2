import requests
import os
import errno
import json
import sys
from string import Template

headers = {'Authorization': f'Bearer {sys.argv[1]}'}

def runQuery(query, headers): 
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f'Query failed to run by returning code of {request.status_code}.')

query = Template('''
{
search(query: "language:Python stars:>100", type: REPOSITORY, first: 99$AFTER) 
  {
  pageInfo {
      hasNextPage
      endCursor
  }
    nodes {
      ... on Repository {
        forks {
          totalCount
        }
        createdAt
        watchers {
          totalCount
        }
        url
        stargazers {
          totalCount
        }
        releases {
          totalCount
        }
        nameWithOwner
        name
        isFork
        primaryLanguage {
          name
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
''')

result = runQuery(query.substitute(AFTER=''), headers)
nodes = result['data']['search']['nodes']
currentPage = 0
hasNextPage  = result['data']['search']['pageInfo']['hasNextPage'] 


while (currentPage < 10 and hasNextPage): 
  cursor = result['data']['search']['pageInfo']['endCursor']
  result = runQuery(query.substitute(AFTER = ', after: \"%s\"' % cursor), headers)
  nodes += result['data']['search']['nodes']
  hasNextPage  = result['data']['search']['pageInfo']['hasNextPage']
  currentPage += 1

filename = 'output.json'
with open(filename, 'w') as file:
  json.dump(nodes, file)

print(f'Written to file {filename}')