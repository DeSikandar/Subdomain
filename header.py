import json
import http
import requests
import requests
from bs4 import BeautifulSoup
# url="cybersecuresoft.com"

def header(url, path='/', method='HEAD'):
	headers = {}
	response = {}
	user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0"
	try:
		conn = http.client.HTTPConnection(url)
		conn.putrequest(method, path)
		conn.putheader("User-Agent", user_agent)
		conn.endheaders()
		res = conn.getresponse()
		conn.close()
		for item in res.getheaders():
			headers.update({item[0]: item[1]})
		
		r=requests.get("http://"+url).text
		soup = BeautifulSoup(r, 'lxml')
		# soup.title

			
		response = {'status': {'code': res.status, 'reason': res.reason}, 'http_headers': headers,'title':soup.title.string}
		response = json.dumps(response, indent=4, separators=(',', ': '))
	except:
		response = {"error":"not founde"}
	
	return response
	# print(response)

# header(url)

