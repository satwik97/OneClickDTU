'''from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage



flow = OAuth2WebServerFlow(
          client_id = CLIENT_ID,
          client_secret = CLIENT_SECRET,
          scope = 'https://spreadsheets.google.com/feeds https://docs.google.com/feeds',
          redirect_uri = 'http://example.com/auth_return'
       )

storage = Storage('creds.data')
credentials = run_flow	(flow, storage)
print "access_token: %s" % credentials.access_token'''



#from google.appengine.ext import vendor
# Add any libraries installed in the "lib" folder.
#vendor.add('lib')
'''import gspread
import datetime
CLIENT_ID = '210116318041-r84j6o2t37gg9car7b3n020svsrjdmk8.apps.googleusercontent.com'

c=gspread.authorize(CLIENT_ID)
c.login()
worksheet = sheet.get_worksheet(0)'''

import httplib2
import json
import gspread
#from google.appengine.api import memcache
#from oauth2client.appengine import AppAssertionCredentials
from oauth2client.client import SignedJwtAssertionCredentials
#from oauth2client.appengine import AppAssertionCredentials

from sys import argv
script , numRows = argv #Enter exact number of rows to parse starting from first row(including title row).


json_key = json.load(open('One Click DTU-1957304b9769.json'))
scope = ['https://spreadsheets.google.com/feeds']

CLIENT_SECRET = 'JjtXFwVe8EIqd5Jqq0OpGgsa'
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

#credentials = AppAssertionCredentials(scope)
#http = credentials.authorize(httplib2.Http(memcache))
gc = gspread.authorize(credentials)
#gc.login()

sheet =gc.open_by_url('https://docs.google.com/spreadsheets/d/1klV5xbwJ_oczb_NYll6Ya-LHY32jRI5tkTmzbrNHkeI/edit#gid=0').get_worksheet(0)
events = []

def parseSpreadsheet(rows):	
	count=1
	for row in range(2,rows+1):
		title = sheet.cell(row,2).value
		etype = sheet.cell(row,3).value
		link = sheet.cell(row,4).value
		#date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.(row,5).value,sheet.datemode))
		#dateString = date.strftime("%a, %d %b")
		date = sheet.cell(row,5).value
		dict = {'title':title,'type':etype,'link':link,'date':date}
		events.append(dict)
		print 'event #'+str(count)+' appended'
		count +=1
	file = open("data.txt",'w')
	file.write(str(events))
	file.close()
	return events
parseSpreadsheet(int(numRows))
	
	