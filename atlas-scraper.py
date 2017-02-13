from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from course import Course
import requests
import time

baseUrl = "http://www.courseatlas.com/SearchCoursesOnline/CourseSearchResults/tabid/135/Default.aspx?instnm=%5bA-Z%5d&distance=5&page={0}&perpage=50"

pages = 10

def getPage(url):
    print("Retrieving URL:\n"+url)
    session = requests.Session()
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    try:
        req = session.get(url, headers=headers)
        if req.status_code is 429:
            time.sleep(1)
            return getPage(url)
    except requests.exceptions.RequestException:
        return None
    bsObj = BeautifulSoup(req.text, "lxml")
    return bsObj

def parseCourse(pageUrl):
    time.sleep(1)
    bsObj = getPage(pageUrl)
    institution = bsObj.find("span",id= "dnn_ctr1713_CourseInfo_Label4")
    subject = bsObj.find("span",id="dnn_ctr1713_CourseInfo_Label14")
    description = bsObj.find("span",id="dnn_ctr1713_CourseInfo_Label16")
    institution = institution.get_text() if institution is not None else ""
    subject = subject.get_text() if subject is not None else ""
    description = description.get_text() if description is not None else ""

    print(institution)
    print(subject)
    print(description)

def getCourses(pageUrl):
    bsObj = getPage(pageUrl)
    courses = bsObj.find("ul",{"class","student-course-search-results-list"}).find_all("li")
    for course in courses:
        parseCourse(course.find("a").attrs["href"])


for page in range(1, pages):
    getCourses(baseUrl.format(page))
