#! python3

#python vs java notes

#python is not designed to have same a classes with same name
#python does not require interfaces it uses multiple inheritance


#python notes
#when referencing a class to an object you must use self on the method
#to use variables on the same class add self



"""psuedocode of requirements
	print("[0] Add Student")
	    #createStudent()
	    #ASK Student Name
	    #Ask If User want to store Grade
	    #IF YES GOTO storeGrade()

	    #Nice to have
	    #ask if user wants to insert another

	#print("[1] Store Grade on Existing Student")
	    #storeGrade()
	    #ASK IF FOR Discussions Forum or Final Project
	    #IF for Discussion Forum or Final Proj
	    #ask for DF Report Grade:
	    #ask for Project Grade
	    #ask for Final Exam Grade

    #print("[2] View Grade of Students for each Assesment")
	    #viewGrades()
	    #ASK IF FOR Discussions Forum or Final Project
	    #view all student grades in Discussions Forum

    #print("[3] View Students with below Average Grade for each Assesment")
	    #viewBelowAveGrades()
	    #ASK IF FOR Discussions Forum or Final Project
	    #view all student grades in Discussions Forum

    #print ("[4] View Report of Students Total Grade for the Semester")
	    #viewSemesterGrade()
	    #view barchart of total grades by totalling:

	    #DF REPORT 20%
	    #Project 30%
	    #Final Exam 50%

	    #on all assesments

    #print("[5] View Report of Students with below Average Grade for the Semester")
	    #viewSemesterLowGrades()
	    #view report of student that are below average for the semester
"""

import turtle

#menu
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
		'Discussion Forum',
		'Final Project'
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


def validateInput(max_entry, user_entry):
	try:
		user_entry_int = int(user_entry)	
	except Exception as e:
		return False
	else:
		if user_entry_int <= max_entry:
			return True
		else:
			return False

#Verify menu objects
menu_obj = Menu()
root_menu = menu_obj.createMenu(range(0,7))
menu_functions = ['showAddStudent()','updateStudentGrades()',
				  'viewLowGrades()','viewTotalGrades()','viewTotalLowGrades()','exitMenu()']

def showRootMenu():
	print('\033[H\033[J') #clear screen
	print('\n\n==================================================================')
	print('\n Welcome! What do you want to do? Please Input Number only!\n');
	print(menu_obj.formatMenu(root_menu))

def exitMenu():
	exit()

def gotoMenu(menu):
	menu_list = menu_obj.menus
	x=0
	for n in menu_list:
		if x==menu:
			exec(menu_functions[x])
			break
		x+=1


showRootMenu()
choice = input('Your Answer: ')
while validateInput(len(root_menu),choice) != True:
	showRootMenu()
	print('Invalid Input please try again\n')
	choice = input('Your Answer: ')
gotoMenu(choice)




#choice = validateInput(max_entry)
#transporter(choice)
