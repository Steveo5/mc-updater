import requests
from requests.exceptions import HTTPError
import wget

basePaperUrl = 'https://api.papermc.io/v2/projects/paper/'

try:
    response = requests.get(basePaperUrl)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()

    latestVersion = jsonResponse['versions'][-1]

    print(latestVersion)

    response = requests.get(basePaperUrl + 'versions/' + latestVersion + '/builds/')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()

    latestBuild = jsonResponse['builds'][-1]['build']
    latestDownload = jsonResponse['builds'][-1]['downloads']['application']['name']

    print(latestBuild)
    print(latestDownload)

    downloadUrl = basePaperUrl + 'versions/' + str(latestVersion) + '/builds/' + str(latestBuild) + '/downloads/' + str(latestDownload)
    print(downloadUrl)
    r = requests.get(downloadUrl, allow_redirects=True)
    open('minecraft_server.jar', 'wb').write(r.content)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')