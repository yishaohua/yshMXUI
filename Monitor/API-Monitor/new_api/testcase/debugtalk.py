import hashlib
import hmac
import json
import random
import string
  

SECRET_KEY = "DebugTalk"

def get_uuid():
    testId = "test_" + str(random.randint(10000,30000))
    return testId
def get_baseurl():
    list1 = ["https://androidapi.mxplay.com","https://androidapi.mxplay.com"]
    base_url = random.choice(list1)
    return base_url

def get_dev_baseurl():
    base_url = "https://androidapi.dev.mxplay.com"
    return base_url
