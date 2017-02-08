from urllib.request import urlopen
from bs4 import BeautifulSoup
from course import Course

baseUrl = "http://www.courseatlas.com/SearchCoursesOnline/CourseSearchResults/tabid/135/Default.aspx?instnm=%5bA-Z%5d&distance=5&page={0}&perpage=50"

pages = 10

def parseCourse(pageUrl):
    print(pageUrl)
    html = urlopen(pageUrl)
    print(html)
    bsObj = BeautifulSoup(html, "lxml")
    info = bsObj.find_all("span",{"id","dnn_ctr1713_CourseInfo_Label4"})
    institution = info[0].getText()
    subject = info[0].getText()
    print(institution)
    print(subject)

def getCourses(pageUrl):
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    courses = bsObj.find("ul",{"class","student-course-search-results-list"}).find_all("li")
    for course in courses:
        parseCourse(course.find("a").attrs["href"])


for page in range(1, pages):
    getCourses(baseUrl.format(page))
