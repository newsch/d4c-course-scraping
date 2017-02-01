class Course:
    '''common base class for all courses'''

    def __init__(self, title, subject, description):
       self.title = title
       self.subject = subject
       self.description = description


    def __str__(self):
        return(self.title + ' in ' + self.subject + '\n' + self.description)
