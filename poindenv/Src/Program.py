import subprocess, os, time
from datetime import datetime
import requests

__author__ = "Florian Schubert"
__copyright__ = ""
__credits__ = [""]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Florian Schubert"
__email__ = ""
__status__ = "Prototype"

'''
date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print("%s Function: Exception occurred during ping\r\n" % (date_time))
'''
apiURL = "https://epin.lgl.bayern.de/api/"
endpointLocations = "locations"
endpointPollen = "pollen"
endpointSeasons = "seasons"
endpointMeasurements = "measurements"

apiRequest = apiURL+endpointLocations

response = requests.get(apiRequest)
print(response.json())