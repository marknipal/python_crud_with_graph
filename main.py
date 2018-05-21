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
	    #ASK IF FOR student ID
	    #ask for DF Report Grade:
	    #ask for Project Grade
	    #ask for Final Exam Grade

    #print("[2] View Grade of Students for each Assesment")
	    #viewGrades()
	    #ASK IF FOR DF, proj or Final Project
	    #view all student grades in Discussions Forum

    #print("[3] View Students with below Average Grade for each Assesment")
	    #viewBelowAveGrades()
	    #ASK IF FOR DF, proj or Final Project
	    #view all student grades in Discussions Forum

    #print ("[4] View Report of Students Total Grade for the Semester")
	    #viewSemesterGrade()
	    #view barchart of total grades by totalling:

	    #DF REPORT 20%
	    #Project 30%
	    #Final Exam 50%


    #print("[5] View Report of Students with below Average Grade for the Semester")
	    #viewSemesterLowGrades()
	    #view report of student that are below average for the semester
"""

import turtle
import os


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
		'Discussion Forum Report',
		'Project'
		'Final Exam'
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
		if user_entry_int < max_entry:
			return True
		else:
			return False

def tryParseInt(x):
	try:
		user_entry_int = int(x)	
	except Exception as e:
		pass
	finally:
		return user_entry_int

def isValidGrade(x):
	try:
		user_entry_int = int(x)	
	except Exception as e:
		return False
	else:
		if user_entry_int <= 100:
			return True
		else:
			return False


#GLOBAL STUDENT OBJECT
students = []

#Verify menu objects
menu_obj = Menu()
current_menu = menu_obj.createMenu(range(0,7))
menu_functions = ['showAddStudent()','updateStudentGrades()',
				  'viewStudentGrade()','viewLowGrades()','viewTotalGrades()',
				  'viewTotalLowGrades()','exitMenu()']

def clrscr():
	print('\033[H\033[J') #clear screen
	windows_clear_screen = os.system("clear") 
	linux_clear_screen = os.system('cls') # on windows
	print('\n\n==================================================================')	

def showRootMenu():
	clrscr()
	print('\n Welcome! What do you want to do? Please Input Number only!\n');
	print(menu_obj.formatMenu(current_menu))

def showAddStudent():
	name = ""
	while name == "":
		clrscr()
		print('\n PLEASE ENTER A VALID Student Name\n');
		choice = input("Your Answer: ")
		name = choice
	valid_grade = False
	while valid_grade != True:
		clrscr()
		print('\n PLEASE ENTER A VALID DF REPORT GRADE MAX 100\n');
		choice = input("Your Answer: ")
		valid_grade = isValidGrade(choice)
	df_grade = valid_grade
	valid_grade = False
	while valid_grade != True:
		clrscr()
		print('\n PLEASE ENTER A VALID Project GRADE MAX 100\n');
		choice = input("Your Answer: ")
		valid_grade = isValidGrade(choice)
	proj_grade = valid_grade
	valid_grade = False
	while valid_grade != True:
		clrscr()
		print('\n PLEASE ENTER A VALID Final Exam GRADE MAX 100\n');
		choice = input("Your Answer: ")
		valid_grade = isValidGrade(choice)
	final_exam_grade = valid_grade

	clrscr()
	students.append([name, df_grade, proj_grade, final_exam_grade])
	print('\n Student SUCCESSFULLY ADDED PRESS ENTER TO GO BACK\n');
	try:
		input("Press enter to continue")
	except SyntaxError:
		pass
	showRootMenu()

def updateStudentGrades():
	clrscr()
	students = ['asdasd',12,23,34]
	x = 0
	for each_student[x] in students:
		print('[{}] Name: {} DF: {} PROJ: {} FINAL: {}').format(x,each_student[0],each_student[1],each_student[2],each_student[3])
		x += 1

def viewLowGrades():
	print("show viewLowGrades form")
def viewTotalGrades():
	print("show viewTotalGrades form")
def viewTotalLowGrades():
	print("show viewTotalLowGrades form")
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


end = False
showRootMenu()
while end != True:
	choice = input('Your Answer: ')
	while validateInput(len(current_menu),choice) != True:
		showRootMenu()
		print('Invalid Input please try again\n')
		choice = input('Your Answer: ')
	gotoMenu(tryParseInt(choice))