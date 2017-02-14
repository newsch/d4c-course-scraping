import pymysql
from pymysql.err import InternalError

class Database:
	"""Class for mySQL databases

	Provide a connection and cursor for all pymysql calls.
	Based on code by Ryan Elizabeth Mitchell.

	"""

	def __init__(self):
		self.conn = pymysql.connect(host='127.0.0.1', unix_socket='/opt/lampp/var/mysql/mysql.sock', user='root', passwd='', charset='utf8')
		self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
		self.cur.execute("USE coursescraping")
