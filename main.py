import os
import urllib.request
import urllib.error
import urllib.parse
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_ua():
    import random
    user_agents = [
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
		"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
		"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
		"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
    ]
    user_agent = random.choice(user_agents)
    return user_agent
  
  
ua = get_ua()
headers = {'User-Agent': ua}
dlurl="https://www.xvideos.com/"
_url = urllib.request.Request(dlurl,headers=headers)
response = urllib.request.urlopen(_url, None, 10)
data=response.read().decode('utf-8')
# print(data)
rule = r'data-id="(.*?)" data-is'
vidList = re.findall(rule, data)
print(vidList)

#https://www.xvideos.com/video{vidList}/_
