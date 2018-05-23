class Menu:
	def __init__(self):
		self.menus = [
		'Add Student', 
		'Store Grade on Existing Student' ,
		'View Grade of Students for each Assesment',
		'View Students with below Average Grade for each Assesment',
		'View Report of Students Total Grade for the Semester',
		'View Report of Students with below Average Grade for the Semester',
		'Exit',
		'Discussion Forum Report Grade',
		'Project Grade',
		'Final Exam Grade',
		'Go Back',
		'Exit',
		'Add another User'
		]

	def createMenu(self,list=[]):
		#TODO Implement One liner here
		x=0
		selected_menus=[]
		for each_menu in self.menus:
			for each_list in list:
				if each_list == x:
					selected_menus.append(each_menu)
			x += 1

		return selected_menus

	def formatMenu(self,list=[]):
		x=0
		formatted_menu=""
		for each_list in list:
			formatted_menu += ('[{0}] {1} \n'.format(x,each_list))
			x += 1
		return formatted_menu