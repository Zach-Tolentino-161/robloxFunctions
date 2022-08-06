import requests
import json
from .Errors.Errors import *
from random import randint
class Users:
  def get_display_by_id(id):
    user_json_url = f"https://users.roblox.com/v1/users/{id}"
    user_json_content = requests.get(str(user_json_url)).text
    user_json = json.loads(user_json_content)
    return user_json["displayName"]
  def get_random_display():
    """
    This will get a random valid roblox display name. If the random user doesn't have a display name, it will give the normal username.
    """
    while True:
      user_id = randint(1, 500000000)
      user_json_url = f"https://users.roblox.com/v1/users/{user_id}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      if user_json['isBanned'] == False:
        return user_json['displayName']
        break
      else:
        continue
  def get_username_by_id(user_id):
    """
  This function will convert your username to a user ID.
    """
    user_json_url = f"https://users.roblox.com/v1/users/{user_id}"
    user_json_content = requests.get(user_json_url).text
    user_json = json.loads(user_json_content)
    return {user_json["name"]}
  def get_id_by_username(username):
    """
  This function will convert your user's ID into a username.
    """
    convert_url = f"https://api.roblox.com/users/get-by-username?username={username}"
    convert_content = requests.get(convert_url).text
    convert_json = json.loads(convert_content)
    return convert_json["Id"]
  def get_display_by_username(username):
    try:
      user_json_url = f"https://users.roblox.com/v1/users/{Users.get_id_by_username(username)}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      return user_json["displayName"]
    except KeyError:
      return 'Invalid username'
  def get_url_by_username(username):
    user_json_url = f"https://users.roblox.com/v1/users/{Users.get_id_by_username(username)}"
    user_json_content = requests.get(user_json_url).text
    user_json = json.loads(user_json_content)
    if user_json['isBanned'] == False:
      return f"https://web.roblox.com/users/{Users.get_id_by_username(user_json['name'])}"
  def get_url_by_id(id):
    user_json_url = f"https://users.roblox.com/v1/users/{id}"
    user_json_content = requests.get(user_json_url).text
    user_json = json.loads(user_json_content)
    if user_json['isBanned'] == False:
      return f"https://web.roblox.com/users/{user_json['id']}"
  def get_random_id():
    """
    This function will give a random valid user ID.
    """
    while True:
      user_id = randint(1, 500000000)
      user_json_url = f"https://users.roblox.com/v1/users/{user_id}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      if user_json['isBanned'] == False:
        print(user_json['id'])
        break
      else:
        continue
  def get_random_url():
    """
    This will get a random valid roblox user's url.
    """
    while True:
      user_id = randint(1, 500000000)
      user_json_url = f"https://users.roblox.com/v1/users/{user_id}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      if user_json['isBanned'] == False:
        return f"https://web.roblox.com/users/{Users.get_id_by_username(user_json['name'])}"
        break
      else:
        continue
  def get_random_user():
    """
    This will get a random valid roblox username.
    """
    while True:
      user_id = randint(1, 500000000)
      user_json_url = f"https://users.roblox.com/v1/users/{user_id}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      if user_json['isBanned'] == False:
        return f"{user_json['name']}"
        break
      else:
        continue
  def get_description_by_id(id):
      user_json_url = f"https://users.roblox.com/v1/users/{id}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      if "error" in user_json:
        return 'Invalid ID'
      elif user_json["description"] == "":
        return 'No description found.'
      else:
        return user_json["description"]
  def get_description_by_user(username):
    try:
      user_json_url = f"https://users.roblox.com/v1/users/{Users.get_id_by_username(username)}"
      user_json_content = requests.get(user_json_url).text
      user_json = json.loads(user_json_content)
      if user_json["description"] == "":
        return 'No description found.'
      else:
        return user_json["description"]
    except KeyError:
      return 'Invalid Username'
  def isBanned_by_user(username):
    try:
      API_URL = f"https://users.roblox.com/v1/users/{Users.get_id_by_username(username)}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      if API_JSON['isBanned'] == True:
        return True
      elif API_JSON['isBanned'] == False:
        return False
    except KeyError:
      raise InvalidUserError(user=username)
  def isBanned_by_id(id):
    try:
      API_URL = f"https://users.roblox.com/v1/users/{id}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      if API_JSON['isBanned'] == True:
        return True
      elif API_JSON['isBanned'] == False:
        return False
    except KeyError:
      raise InvalidUserError(user=id)