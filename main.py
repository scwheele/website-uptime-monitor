import requests
import time
import json

def test_website(url, method):
    curTime = int(round(time.time() * 1000))

    if method == "get":
        r = requests.get(url)
    elif method == "post":
        r = requests.post(url)
    else:
        print('Invalid method, supported methods are GET and POST')

    status_code = r.status_code
    doneTime = int(round(time.time() * 1000))
    responseTime = (doneTime - curTime)
    returnData = {'url': url, 'responseCode': status_code, 'responseTime': responseTime }

    return returnData

def load_config():
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)

    return data

if __name__ == "__main__":
    
    configData = load_config()

    for key in configData:
        value = configData[key]

        url = value["url"]
        method = value["method"]
        expectStatus = value["expectStatus"]
        maxLatency = value["maxLatency"]

        responseData = test_website(url, method)

        if responseData['responseCode'] != expectStatus:
            print("ERROR: Unexpected status")
        else:
            print("Status is good!")

        if responseData["responseTime"] >= maxLatency:
            print("ERROR: Unexpected latency")
        else:
            print("Latency is fine!")

        print(responseData)

    pass