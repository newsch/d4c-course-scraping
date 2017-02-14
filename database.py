import pymysql
from pymysql.err import InternalError

class Database:

	def __init__(self):
		#Assumes port 3306
		self.conn = pymysql.connect(host='127.0.0.1', unix_socket='/opt/lampp/var/mysql/mysql.sock', user='root', passwd='', charset='utf8')
		self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
		self.cur.execute("USE coursescraping")
