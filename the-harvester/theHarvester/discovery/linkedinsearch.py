import string
import httplib, sys
import myparser
import re

class search_linkedin:
	def __init__(self,word,limit):
		self.word=word.replace(' ', '%20')
		self.results=""
		self.totalresults=""
		self.server="www.google.com"
		self.hostname="www.google.com"
		self.userAgent="(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
		self.quantity="100"
		self.limit=int(limit)
		self.counter=0
		
	def do_search(self):
		h = httplib.HTTP(self.server)
		h.putrequest('GET', "/search?num=100&start=" + str(self.counter) + "&hl=en&meta=&q=site%3Alinkedin.com%20" + self.word)
		h.putheader('User-agent', self.userAgent)	
		h.endheaders()
		returncode, returnmsg, headers = h.getreply()
		self.results = h.getfile().read()
		self.totalresults+= self.results

	def get_people(self):
		rawres=myparser.parser(self.totalresults,self.word)
		return rawres.people_linkedin()
	
	def process(self):
		while (self.counter < self.limit):
			self.do_search()
			self.counter+=100
			print "\tSearching "+ str(self.counter) + " results.."
