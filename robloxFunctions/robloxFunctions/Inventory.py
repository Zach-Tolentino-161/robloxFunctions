import requests, json
from .Users import Users
from .Errors.Erors import *
class Inventory:
  def is_owned_by_user(username, itemType, assetID):
    """
    The itemType can be an asset, gamepass, bundle and a badge.
  This function will return True or False.
    """
    USERNAME_URL_CHECK = f"https://users.roblox.com/v1/users/{Users.get_id_by_username(username)}"
    USERNAME_CONTENT = requests.get(USERNAME_URL_CHECK).text
    if "error" in USERNAME_CONTENT:
      raise InvalidUserError(user=username)
    elif itemType == "Asset" or itemType == "asset":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/Asset/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidAssetIDError(asset=assetID)
    elif itemType == "Badge" or itemType == "badge":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/Badge/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidBadgeIDError(badge=assetID)
    elif itemType == "gamepass" or itemType == "Gamepass":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/GamePass/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidPassError(gamePass=assetID)
    elif itemType == "bundle" or itemType == "Bundle":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/Bundle/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidBundleIDError(bundle=assetID)
    else:
      return 'Invalid ItemType'
  def is_owned_by_id(id, itemType, assetID):
    """
  The itemType can be an asset, gamepass, bundle and a badge.
  This function will return True or False.
    """
    USERID_URL_CHECK = f"https://users.roblox.com/v1/users/{id}"
    USERID_CONTENT = requests.get(USERID_URL_CHECK).text
    if "error" in USERID_CONTENT:
      raise InvalidUserIDError(userID=id)
    elif itemType == "Asset" or itemType == "asset":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/Asset/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidAssetIDError(asset=assetID)
    elif itemType == "Badge" or itemType == "badge":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/Badge/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidBadgeIDError(badge=assetID)
    elif itemType == "gamepass" or itemType == "Gamepass":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/GamePass/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        raise InvalidPassError(gamePass=assetID)
    elif itemType == "bundle" or itemType == "Bundle":
      try:
        API_URL = f"https://inventory.roblox.com/v1/users/{id}/items/Bundle/{assetID}/is-owned"
        API_CONTENT = requests.get(API_URL).text
        if "false" in API_CONTENT:
          return False
        else:
          return True
      except KeyError:
        return 'Invalid BundleID'
    else:
      return 'Invalid ItemType'
  def can_view_inventory_by_user(username):
    try:
      API_URL = f"https://inventory.roblox.com/v1/users/{Users.get_id_by_username(username)}/can-view-inventory"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      if API_JSON["canView"] == True:
        return True
      else:
        return False
    except KeyError:
      return 'Invalid Username'
  def can_view_inventory_by_id(id):
    API_URL = f"https://inventory.roblox.com/v1/users/{id}/can-view-inventory"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    if "error" in API_CONTENT:
      return 'Invalid UserID'
    elif API_JSON["canView"] == True:
      return True
    else:
      return False