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
    #list1 = ["http://13.232.52.127:5000"]
    base_url = random.choice(list1)
    return base_url

def get_dev_baseurl():
    base_url = "https://androidapi.dev.mxplay.com"
    return base_url

def get_auth():
    auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IntmYn17MTE5OTE5NDMyMTk0MzE3fSJ9.0hKFlWX28xNicM5CxcUYb2LjlydynpLce-2HZjNTPfw"
    return auth 

def get_dev_auth():
    auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IntmYn17MTkxODkzOTI4MzMwMjAwfSIsImNyZWF0aW1lIjoxNTM0OTAyNjUzfQ.XeKxA2lJPQq-fJYF5jVJMCTbOEYRLp5gPkzhhbwG6ms"
    return auth 
