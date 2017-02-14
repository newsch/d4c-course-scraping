# d4c-course-scraping

## About
This project is a python tool to scrape course catalogs of educational institutions. Created for the "Working the Data Science Process with Python" (Dirty Data Done Dirt Cheap) seminar taught by Ryan Elizabeth Mitchell (@REMitchell) in Spring 2017 at @Olin College of Engineering.

## Getting Started
1. You'll need Python 3, a running mySQL installation, and the relevant [third-party libraries](#Third-Party-Libraries-Used) installed.

2. Edit [database.py](database.py) to match your mySQL installation's user, password, host, socket, etc.

3. Run [atlas-scraper.py](atlas-scraper.py) to begin scraping!

## Contributors
Evan Lloyd New-Schmidt (@newsch), first-year student at @Olin  
Tobias Schapinsky (@TShapinsky), first-year student at @Olin  
Mel Chua (@mchua), an @Olin alumni  
Yichen Jiang (@yjiang0929), first-year student at @Olin  

## Third Party Libraries Used
- BeautifulSoup, lxml, and Requests for scraping
- pymysql for storing data
