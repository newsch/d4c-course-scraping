class Website:
	'Common base class for all articles/pages'


	def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, pageTitle, pageBody):
		self.name = name
		self.url = url
		self.searchUrl = searchUrl
		self.resultListing = resultListing
		self.resultUrl = resultUrl
		self.absoluteUrl=absoluteUrl

		#prepend a slash to relative URLs if not already done
		if absoluteUrl == "FALSE" and resultUrl[0]!='/':
			self.resultUrl = '/' + self.resultUrl

		print("resultUrl is", self.resultUrl)	
		self.pageTitle = pageTitle
		self.pageBody = pageBody
