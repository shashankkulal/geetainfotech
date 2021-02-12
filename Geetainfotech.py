import requests


def getSpeed(page):
    key = "AIzaSyAWkTAsGwimWkqrug9C0Rw3o9Yfs89yuNI"
    apiUrl = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
    strategy = 'desktop'

    response_url = apiUrl + page + '&key=' + key + '&strategy=' + strategy
    response = requests.get(response_url)
    json_data = response.json()

    lighthouseResult = json_data["lighthouseResult"]
    categories = lighthouseResult["categories"]
    performance = categories["performance"]
    score = performance["score"]
    score = str(score * 100)
    #print(page + ":" + str(score * 100))
    return {'url' : page, 'score' : score}

