from pymysql.err import InternalError
class Course:
	'''common base class for all courses'''

	def __init__(self, id, title, subject, description, institution):
		self.id = id
		self.title = title
		self.subject = subject
		self.description = description
		self.institution = institution


	def __str__(self):
		return(self.title + ' in ' + self.subject + ' at ' + self.institution + '\n' + self.description)


	def save(self, db):
		try:
			db.cur.execute("SELECT * FROM courses WHERE title = %s AND subject = %s AND institution = %s AND description = %s", (self.title, self.subject, self.institution, self.description))

			if db.cur.rowcount == 0:
				values = dict(vars(self))
				for value in values:
					if values[value] == '':
						values[value] = 'NULL'
					else:
						values[value] = "'%s'" % values[value]
				print(self)
				db.cur.execute("INSERT INTO courses (title, subject, institution, description) VALUES (%(title)s, %(subject)s, %(institution)s, %(description)s)", values)
				db.conn.commit()
				self.id = db.cur.lastrowid
			else:
				self.id = db.cur.fetchall()[0]["id"]

		except InternalError as e:
			print("INSERT INTO courses (title, subject, institution, description) VALUES ("+str(self.title)+", "+str(self.subject)+", "+str(self.institution)+", "+str(self.description)+")")

			print("Internal error!")
			print(e)
			db.conn.rollback()


		return self
