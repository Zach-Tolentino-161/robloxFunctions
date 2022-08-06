from .Users import Users
from .Errors.Exceptions import *
import requests, json
class Games:
  def get_universe_id(gameID):
    API_URL = f"https://api.roblox.com/universes/get-universe-containing-place?placeid={gameID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    if "error" in API_JSON:
      return 'Invalid PlaceID'
    else:
      return API_JSON['UniverseId']
  def get_place_id_by_universe_id(universeID):
    """
    This function will convert the PlaceID to the UniverseID. 
    """
    API_URL = f"https://games.roblox.com/v1/games?universeIds={universeID}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return ['data'][0]['id']
  def get_game_description_by_id(gameID):
    try:
      API_URL = f"https://games.roblox.com/v1/games?universeIds={Games.get_universe_id(gameID)}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      return API_JSON['data'][0]["description"]
    except KeyError:
      raise 
  def get_game_name_by_id(gameID):
    try:
      API_URL = f"https://games.roblox.com/v1/games?universeIds={Games.get_universe_id(gameID)}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      return API_JSON['data'][0]["name"]
    except KeyError:
      return 'Invalid GameID'
  def get_owner_of_game_by_id(gameID):
    try:
      API_URL = f"https://games.roblox.com/v1/games?universeIds={Games.get_universe_id(gameID)}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      return API_JSON['data'][0]['creator']["name"]
    except KeyError:
      return 'Invalid GameID'
  def get_playing_count_by_id(gameID):
    try:
      API_URL = f"https://games.roblox.com/v1/games?universeIds={Games.get_universe_id(gameID)}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      return API_JSON['data'][0]["playing"]
    except KeyError:
      return 'Invalid UniverseID'
  def get_visits_by_id(gameID):
    try:
      API_URL = f"https://games.roblox.com/v1/games?universeIds={Games.get_universe_id(gameID)}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      return API_JSON['data'][0]['visits']
    except KeyError:
      return 'Invalid GameID'
  def get_placeid_by_universeid(universeID):
    try:
      API_URL = f"https://games.roblox.com/v1/games?universeIds={universeID}"
      API_CONTENT = requests.get(API_URL).text
      API_JSON = json.loads(API_CONTENT)
      return API_JSON["data"][0]["rootPlaceId"]
    except KeyError:
      return 'Invalid UniverseID'

def get_game_owner_type_by_id(gameID):
  """
  This function will get the owner of the game's type, it can be a Group or a User.
  """
  try:
    API_URL = f"https://games.roblox.com/v1/games?universeIds={Games.get_universe_id(gameID)}"
    API_CONTENT = requests.get(API_URL).text
    API_JSON = json.loads(API_CONTENT)
    return API_JSON['data'][0]['creator']['type']
  except KeyError:
    return 'Invalid PlaceID'