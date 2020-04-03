import requests
from json import dump
from json import loads
import os
import errno
import json
from csv import DictWriter


headers = {"Authorization": "Bearer 4ff4ab9e077b11a6839403c927d6dd5303cf6a8b"} 

def runQuery(query, headers): 
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}.".format(request.status_code))

query = """
query lab2S2 {
  search(query: "stars:>100 language:Python", type: REPOSITORY, first: 20{AFTER}) {
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
"""

finalQuery = query.replace("{AFTER}", "")
result = runQuery(finalQuery, headers)
nodes = result['data']['search']['nodes']
conta_repositorios_python = 0
total_pages =0
next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"] 


while (total_pages < 1000 and next_page): 
    cursor = result["data"]["search"]["pageInfo"]["endCursor"]
    next_query = query.replace("{AFTER}", ", after: \"%s\"" % cursor)
    result = runQuery(next_query, headers)
    nodes += result['data']['search']['nodes']
    next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"]
    total_pages += 1  

filename = 'pythonrepo.json'
with open('pythonrepo.json', 'w') as file:
  json.dump([node for node in nodes if node['primaryLanguage'] is not None and node['primaryLanguage']['name'] == 'Python' and node['isFork'] != True], file)

print('Written to file pythonrepo.json')