import webapp2
from google.appengine.ext import vendor
# Add any libraries installed in the "lib" folder.
vendor.add('lib')
import jinja2
import os 
import cgi
import datetime
import requests



file = open("data.txt",'r')
eventData =eval(file.read().replace('\n',' '))


today = datetime.datetime.today()
today = today.strftime("%d %b")

template_dir = os.path.join(os.path.dirname(__file__), 'templates')


root_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader([template_dir,root_dir]),autoescape=True)


def escapeHTML(string):
	return cgi.escape(string , quote="True")

	
class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
		#self.response.write(form %{"error":error})
		self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
		t = jinja_env.get_template(template)
		return t.render(params)		
    def render(self , template ,**kw):
		self.write(self.render_str(template,**kw))

class IndexHandler(Handler):
		
		def get(self):
			self.render("index.html",events=eventData,today=today)
			
		
class AboutHandler(Handler):
	def get(self):
		self.render("about.html")
		
class LoginHandler(Handler):
	def get(self):
		self.render("login.html")
		
class AdminHandler(Handler):
	def post(self):
		pwd=self.request.get('pwd')
		if(pwd=='update'):
			rows=self.request.get('rows')
			parse_sheet.parse(rows)
			self.response.out.write("update successful!")
		else:
			self.response.write("Incorrect Password")
			
class AddEventHandler(Handler):
	def get(self):
		self.render("addEvent.html")
		
class LibraryHandler(Handler):
	def post(self):
		libraryID = self.request.get('libraryID')
		response = requests.post('http://14.139.251.99:8080/jopacv06/html/memberlogin',data={'txtmemberid':libraryID,'txtmemberpwd':''})
		if(response.status_code==200):
			html_doc = response.text
			#self.response.out.write(html_doc)
		else:
			self.response.write("Sorry , either your inputs were not correct or some internal error occured!")
		self.redirect('http://14.139.251.99:8080/jopacv06/html/memberlogin')

app = webapp2.WSGIApplication([('/', IndexHandler),("/about",AboutHandler),("/admin",AdminHandler),("/addEvent",AddEventHandler),("/library",LibraryHandler)], debug=True)
