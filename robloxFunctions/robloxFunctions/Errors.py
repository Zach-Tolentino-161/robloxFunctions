import traceback, sys
def myexcepthook(type, value, tb):
    l = ''.join(traceback.format_exception(type, value, tb))
    print(l)
sys.excepthook = myexcepthook
class Exceptions:
  class InvalidUserError(Exception):
    def __init__(self, user, **message):
      self.user = user
      default_message = f"{self.user} is an invalid user."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidUserIDError(Exception):
    def __init__(self, userID, **message):
      self.userID = userID
      default_message = f"{self.userID} is an invalid userID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class UserIsBannedError(Exception):
    def __init__(self, user, **message):
      self.user = user
      default_message = f"{self.user} is a banned user."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class UserIDIsBannedError(Exception):
    def __init__(self, userID, **message):
      self.userID = userID
      default_message = f"{self.userID} is a banned userID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidUserIDError(Exception):
    def __init__(self, userID, **message):
      self.userID = userID
      default_message = f"{self.userID} is an invalid userID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidGameError(Exception):
    def __init__(self, game, **message):
      self.game = game
      default_message = f"{self.game} is an invalid gameID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidAssetIDError(Exception):
    def __init__(self, asset, **message):
      self.asset = asset
      default_message = f"{self.asset} is an invalid assetID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidBundleIDError(Exception):
    def __init__(self, bundle, **message):
      self.bundle = bundle
      default_message = f"{self.bundle} is an invalid bundleID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidGroupError(Exception):
    def __init__(self, group, **message):
      self.group = group
      default_message = f"{self.group} is an invalid groupID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidPassError(Exception):
    def __init__(self, gamePass, **message):
      self.gamePass = gamePass
      default_message = f"{self.gamePass} is an invalid gamePassID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)
  class InvalidBadgeIDError(Exception):
    def __init__(self, badge, **message):
      self.badge = badge
      default_message = f"{self.badge} is an invalid badgeID."   
      if message:
        super().__init__(message)
      else:
        super().__init__(default_message)