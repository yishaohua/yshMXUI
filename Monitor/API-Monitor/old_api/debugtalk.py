import hashlib
import hmac
import json
import random
import string
  

SECRET_KEY = "DebugTalk"

def get_uuid():
    uuId = "test_" + "".join(random.sample(string.ascii_lowercase + string.digits, 39))
    return uuId

