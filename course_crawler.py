from course import Course

import requests
from bs4 import BeautifulSoup
import sys
from io import StringIO
import csv

class Crawler:
	conn = None
	cur = None


	################
	# Utilty function used to get a Beautiful Soup object
	# from a given URL
	##############
	def getPage(self, url):
		print("Retrieving URL:\n"+url)
		session = requests.Session()
		headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
		try:
			req = session.get(url, headers=headers)
		except requests.exceptions.RequestException:
			return None
		bsObj = BeautifulSoup(req.text, "lxml")
		return bsObj


   	################
	# Utilty function used to get a content string from a Beautiful Soup
	# object and a selector. Returns an empty string if no object
	# is found for the given selector
	##############
	def safeGet(self, pageObj, selector):
		childObj = pageObj.select(selector)
		if childObj is not None and len(childObj) > 0:
			return childObj[0].get_text()
		return ""


	def getCourses(self, pageObj):
		'''Returns a list of Course objects from the given page'''
		subject = pageObj.find('h1', {'class':'page-title'}).getText()
		raw_courses = pageObj.findAll('div', {'class':'courseblock'})
		courses = []
		for raw_course in raw_courses:
			title = str(raw_course.find('h4', {'class':'courseblocktitle'}).getText())
			description = raw_course.find('p', {'class':'courseblockdesc'}).getText()
			courses.append(Course(title, subject, description))


		return(courses)


url = 'http://catalog.mit.edu/subjects/'
crawler = Crawler()
# subject_page = crawler.getPage(url)
# subject_links = subject_page.find('div', {'class':'sitemap'}).findAll('a')
# print(subject_links)
# for subject in subject_links:
# 	if 'Engineering' in subject.getText():
# 		print(subject.getText())
# 		subject_page = 'http://catalog.mit.edu' + subject.attrs['href']
# 		crawler.getCourses(crawler.getPage(subject_page))

sample_subject = crawler.getPage('http://catalog.mit.edu/subjects/16/')
for course in crawler.getCourses(sample_subject):
	print(type(course.title))
