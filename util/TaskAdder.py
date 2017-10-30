__author__ = 'George'
import requests
import hashlib
import json

BASE_URL = 'https://api.rememberthemilk.com/services/rest/'

API_KEY = '197c9c36d9bede2757b20037e86b8e25'
API_SECRET = 'a408c8a1c8d7a31a'
AUTH_TOKEN = 'ce631190488b4a0eef45b85d31b95bde6f988e9a'

AUTH_TOKEN_PARAM = "auth_token"
METHOD_PARAM = "method"
APIKEY_PARAM = "api_key"
TIMELINE_PARAM = "timeline"
APISIGNATURE_PARAM = "api_sig"
FROB_PARAM = "frob"

def get_list():
    method = "rtm.lists.getList"
    frob = get_frob()
    args = []
    args.append([METHOD_PARAM, method])
    args.append([FROB_PARAM, frob])
    args.append(["format", "json"])
    args.append(["perms", "read"])
    args.append(["auth_token", AUTH_TOKEN])
    print(call_and_get_response_include_api_data(args))

def get_frob():
    method = "rtm.auth.getFrob"
    args = []
    args.append([METHOD_PARAM, method])
    args.append(["format", "json"])
    response = call_and_get_response_include_api_data(args)
    json_data = json.loads(response)

    return json_data['rsp']['frob']

def get_auth_token():
    method = "rtm.auth.getToken"
    frob = "8ae698fde702a15b958c40a8e4af62424a851f68"
    args = []
    args.append([METHOD_PARAM, method])
    args.append([FROB_PARAM, frob])
    args.append(["format", "json"])
    response = call_and_get_response_include_api_data(args)
    print(response)


def add_item(item):
    method = "rtm.tasks.add"
    frob = get_frob()
    timeline = get_timeline()
    args = []
    args.append([METHOD_PARAM, method])
    args.append([FROB_PARAM, frob])
    args.append(["format", "json"])
    args.append(["name", item])
    args.append([AUTH_TOKEN_PARAM, AUTH_TOKEN])
    args.append([TIMELINE_PARAM, timeline])
    response = call_and_get_response_include_api_data(args)

    if 'rsp' in json.loads(response):
        return True
    else:
        return False


def get_timeline():
    method = "rtm.timelines.create"
    frob = get_frob()
    args = []
    args.append([METHOD_PARAM, method])
    args.append([FROB_PARAM, frob])
    args.append(["format", "json"])
    args.append([AUTH_TOKEN_PARAM, AUTH_TOKEN])
    response = call_and_get_response_include_api_data(args)
    return json.loads(response)['rsp']['timeline']

def authenticate_user(permission):
    # frob = get_frob()
    url = "https://www.rememberthemilk.com/services/auth/"
    url += "?" + APIKEY_PARAM + "=" + API_KEY

    # url += "&" + "frob=" + frob
    url += "&" + "perms=" + permission

    # + "frob" + frob
    sig_string = API_SECRET + APIKEY_PARAM + API_KEY  + "perms" + permission
    signature = hashlib.md5(sig_string.encode("utf-8")).hexdigest()

    url += "&" + APISIGNATURE_PARAM + "=" + signature
    print(url)
    # response = requests.get(url).text

# Auto-includes API_SECRET and API_KEY
def call_and_get_response_include_api_data(args_as_list):
    args_as_list.append([APIKEY_PARAM, API_KEY])
    args_as_list.sort()

    api_sig_solution = API_SECRET
    url = BASE_URL + "?"

    for current_arg in args_as_list:
        api_sig_solution = api_sig_solution + current_arg[0] + current_arg[1]

    signature = hashlib.md5(api_sig_solution.encode("utf-8")).hexdigest()

    args_as_list.append([APISIGNATURE_PARAM, signature])
    args_as_list.sort()

    for current_arg in args_as_list:
        url = url + "&" + current_arg[0] + "=" + current_arg[1]

    return requests.get(url).text


# print(get_frob())
# get_list()
# get_auth_token()

# print(get_timeline())
add_item("test_message")
# authenticate_user("write")
# add_task("test_name", "test_notes")