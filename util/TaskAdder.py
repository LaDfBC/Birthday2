__author__ = 'George'
import requests
import hashlib

BASE_URL = 'https://api.rememberthemilk.com/services/rest/'


METHOD_PARAM = "method"
APIKEY_PARAM = "api_key"
APISIGNATURE_PARAM = "api_sig"

def get_list():
    args = {}
    method = "rtm.lists.getList"
    args[APIKEY_PARAM] = API_KEY
    args[METHOD_PARAM] = method
    args["format"] = "json"
    print(requests.get(BASE_URL, args))

def test():
    args = {}
    method = "rtm.test.echo"
    args[APIKEY_PARAM] = API_KEY
    args[METHOD_PARAM] = method
    args["format"] = "json"
    api_sig = APIKEY_PARAM + API_KEY + METHOD_PARAM
    print(requests.get(BASE_URL +
                            "?" +
                            "method=" + method + "&" +
                            "api_key" + api_key + "&" +
                            "format=json").text)

def get_frob():
    args = {}
    method = "rtm.auth.getFrob"
    args[APIKEY_PARAM] = API_KEY
    args[METHOD_PARAM] = method
    api_sig_solution = API_SECRET + APIKEY_PARAM + API_KEY + METHOD_PARAM + method
    signature = hashlib.md5(api_sig_solution.encode("utf-8"))
    url = BASE_URL + "?" + \
                       APIKEY_PARAM + "=" + API_KEY + "&" + \
                       APISIGNATURE_PARAM + "=" + signature.hexdigest() + "&" + \
                       METHOD_PARAM + "=" + method
    print(url)
    print(requests.get(url).text)

get_frob()
# get_list()


# add_task("test_name", "test_notes")