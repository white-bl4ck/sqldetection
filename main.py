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
status_detecting = []
error_403_500 = 0
response_list = []
success = 0

# url=input('Enter url')
ur = urlparse('http://localhost/adsdsa?dasdadas=22&das=12')
url = ur.scheme+ '://'+ur.hostname+ur.path
user_agent=user_agent_def()
query = dict(x.split("=") for x in ur.query.split('&'))
for key,item in query.items():
    for iii in detection:
        query_sqli[key]=str(item)+iii
        response = req.get(url,params = query_sqli,headers = user_agent)
        status_detecting.append("query: " + key + "=" + str(item)+iii + " || " + "status: " + str(response.status_code))
        response_list.append(response.text)

for i in status_detecting:
    if '403' in i or '500' in i:
        error_403_500 += 1
    elif '200' in i:
        success += 1

print("errors: " + str(error_403_500) + " And success: " +str(success)+" times")

for i in response_list:
    if "sql" in i:
        print("vulnerable")


# print(url+)


# response = req.get(url,params = query,headers = user_agent)

# print(response.status_code)