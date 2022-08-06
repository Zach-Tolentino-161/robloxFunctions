import requests, json
def get_group_description_by_id(groupID):
  try:
    API_URL = f"https://groups.roblox.com/v1/groups/{groupID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return API_JSON['description']
  except KeyError:
    return 'Invalid GroupID'
def get_group_name_by_id(groupID):
  try:
    API_URL = f"https://groups.roblox.com/v1/groups/{groupID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return API_JSON['name']
  except KeyError:
    return 'Invalid GroupID'
def get_group_owner_by_id(groupID):
  try:
    API_URL = f"https://groups.roblox.com/v1/groups/{groupID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return API_JSON['owner']['name']
  except KeyError:
    return 'Invalid GroupID'
def get_group_owner_display_by_id(groupID):
  try:
    API_URL = f"https://groups.roblox.com/v1/groups/{groupID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return API_JSON['owner']['displayName']
  except KeyError:
    return 'Invalid GroupID'
def get_group_owner_username_by_id(groupID):
  try:
    API_URL = f"https://groups.roblox.com/v1/groups/{groupID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return API_JSON['owner']['username']
  except KeyError:
    return 'Invalid GroupID'