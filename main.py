from email import header
from operator import itemgetter
from re import I
from urllib import response
from urllib.parse import urlparse
import requests as req
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

def user_agent_def():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agents = user_agent_rotator.get_user_agents()
    return {'User-Agent':user_agent_rotator.get_random_user_agent()}
def detection_def():
    detection =[]
    with open('testing.txt','r') as sql_test_file:
        for i in sql_test_file:
            detection.append(i.strip())
        return detection


#vars
detection = detection_def()
query_sqli = {}

# url=input('Enter url')
ur = urlparse('http://localhost:8080/adsdsa?dasdadas=22&das=12')
url = ur.scheme+ '://'+ur.netloc+ur.path
user_agent=user_agent_def()
query = dict(x.split("=") for x in ur.query.split('&'))
for key,item in query.items():
    for iii in detection:
        query_sqli[key]=str(item)+iii
        response = req.get(url,params = query_sqli,headers = user_agent)
        
        # print(url+)

    
# response = req.get(url,params = query,headers = user_agent)

print(response.status_code)