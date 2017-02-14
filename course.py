from pymysql.err import InternalError
class Course:
	"""Class for courses

	Attributes:
		id (int): id for mySQL purposes
		title (str): full title of the course
		subject (str): subject the course is listed under
		description (str): full description of the course
		institution (str): the institution the course is listed under

	"""

	def __init__(self, id, title, subject, description, institution):
		self.id = id
		self.title = title
		self.subject = subject
		self.description = description
		self.institution = institution


	def __str__(self):
		"""Format the object nicely for print() statements"""
		return(self.title + ' in ' + self.subject + ' at ' + self.institution + '\n' + self.description)


	def save(self, db):
		"""Save the object to the provided database

		Checks to see if an identical entry already exists in the database and
		either assigns that existing entry's id to itself or writes a new entry
		to the database and assigns the new entry's id to itself.
		Based on code by Ryan Elizabeth Mitchell.

		Attributes:
			db (Database): mySQL database for object to be saved to

		"""
		try:
			db.cur.execute("SELECT * FROM courses WHERE title = %s AND subject = %s AND institution = %s AND description = %s", (self.title, self.subject, self.institution, self.description))

			if db.cur.rowcount == 0:
				values = dict(vars(self))
				# for value in values:
				# 	if values[value] == '':
				# 		values[value] = 'NULL'
				print(self)
				db.cur.execute("INSERT INTO courses (title, subject, institution, description) VALUES (%(title)s, %(subject)s, %(institution)s, %(description)s)", values)
				db.conn.commit()
				self.id = db.cur.lastrowid
			else:
				self.id = db.cur.fetchall()[0]["ID"]
				print('Ignoring duplicate entry')

		except InternalError as e:
			print("INSERT INTO courses (title, subject, institution, description) VALUES ("+str(self.title)+", "+str(self.subject)+", "+str(self.institution)+", "+str(self.description)+")")

			print("Internal error!")
			print(e)
			db.conn.rollback()


		return self
