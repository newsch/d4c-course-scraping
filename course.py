class Course:
    '''common base class for all courses'''

    def __init__(self, title, subject, description, college):
       self.title = title
       self.subject = subject
       self.description = description
       self.college = college


    def __str__(self):
        return(self.title + ' in ' + self.subject + ' at ' + self.college + '\n' + self.description)
