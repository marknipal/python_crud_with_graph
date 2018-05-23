#! python3

from turtle import Turtle, Screen
from functools import reduce
from Menu import *
import os

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

def tryParseFloat(x):
	try:
		user_entry_int = float(x)	
	except Exception as e:
		pass
	finally:
		return user_entry_int

def isValidInt(x):
	try:
		user_entry_int = int(x)	
	except Exception as e:
		return False
	else:
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

def getAverage(number_list):
	ave = reduce(lambda x, y: x + y, number_list) / len(number_list)
	return ave

#GLOBAL STUDENT OBJECT
students = [["Mylyn",78,80,90],["Catalina",10,40,20]]

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
	print('\n Welcome! What do you want to do? Please Input Number only!\n')
	print(menu_obj.formatMenu(current_menu))

def showAddStudent():
	name = ""
	while name == "":
		clrscr()
		print('\n PLEASE ENTER A VALID Student Name\n')
		choice = input("Your Answer: ")
		name = choice

	valid_grade = False
	while valid_grade != True:
		clrscr()
		print('\n PLEASE ENTER A VALID DF REPORT GRADE MAX 100\n')
		choice = input("Your Answer: ")
		valid_grade = isValidGrade(choice)
	df_grade = choice

	valid_grade = False
	while valid_grade != True:
		clrscr()
		print('\n PLEASE ENTER A VALID Project GRADE MAX 100\n')
		choice = input("Your Answer: ")
		valid_grade = isValidGrade(choice)
	proj_grade = choice

	valid_grade = False
	while valid_grade != True:
		clrscr()
		print('\n PLEASE ENTER A VALID Final Exam GRADE MAX 100\n')
		choice = input("Your Answer: ")
		valid_grade = isValidGrade(choice)
	final_exam_grade = choice

	clrscr()
	students.append([name, df_grade, proj_grade, final_exam_grade])
	print('\n Student SUCCESSFULLY ADDED PRESS ENTER TO GO BACK\n')
	try:
		input("Press enter to continue")
	except SyntaxError:
		pass
	showRootMenu()

def updateStudentGrades():
	clrscr()
	print("\nPLEASE TYPE THE NUMBER OF THE STUDENT YOU WANT TO EDIT BELOW\n")

	if students	== []:
		clrscr()
		print('\n THERE ARE NO CURRENTLY REGISTERED STUDENT PRESS ENTER TO GO BACK\n')
		try:
			input("Press enter to continue")
		except SyntaxError:
			pass
		showRootMenu()
	else:
		choice = None
		x = 0
		while validateInput(x+1,choice) != True:
			x=0
			clrscr()
			print("\nPLEASE TYPE THE NUMBER OF THE STUDENT YOU WANT TO EDIT BELOW\n")
			for each_student in students:
				print('[{}] {} DF: {} PROJ: {} FINAL: {}'.format(x,each_student[0],each_student[1],each_student[2],each_student[3]))
				x += 1
			print ("[{}] GO BACK".format(x))
			choice = input("\nYour Answer: ")
			selected_id = tryParseInt(choice)
			if tryParseInt(choice) == x:
				showRootMenu()
			else:
				clrscr()
				print("\nCurrent Selected Record is")
				x = 0
				for each_student in students:
					if tryParseInt(choice) == x:
						print('\n Student ID: {}\n Name: {}\n Discussion Forum Report Grade: {}\n Project Grade: {} \n Final Exam Grade: {}'.format(x,each_student[0],each_student[1],each_student[2],each_student[3]))
						break;
					x += 1
				print("\nChoose the grade you want to edit\n")
				print(menu_obj.formatMenu(menu_obj.createMenu([7,8,9,10])))

				choice = input("Your Answer: ")

				while tryParseInt(choice) > 3:
					clrscr()
					print("\nCurrent Selected Record is")
					x = 0
					for each_student in students:
						if tryParseInt(selected_id) == x:
							print('\n Student ID: {}\n Name: {}\n Discussion Forum Report Grade: {}\n Project Grade: {} \n Final Exam Grade: {}'.format(x,each_student[0],each_student[1],each_student[2],each_student[3]))
							break;
						x += 1
					print("\nChoose the grade you wanted to edit\n")
					print(menu_obj.formatMenu(menu_obj.createMenu([7,8,9])))
					choice = input("Your Answer: ")
				clean_choice = tryParseInt(choice)
				if clean_choice == 0:
					valid_grade = False
					while valid_grade != True:
						clrscr()
						print('\n PLEASE ENTER THE NEW VALID DF REPORT GRADE MAX 100\n')
						choice = input("Your Answer: ")
						valid_grade = isValidGrade(choice)
					df_grade = tryParseInt(choice)
					students[selected_id][1] = df_grade
					clrscr()
					print('\n Student SUCCESSFULLY ADDED PRESS ENTER TO GO BACK\n')
					try:
						input("Press enter to continue")
					except SyntaxError:
						pass
					updateStudentGrades()
				elif clean_choice == 1:
					valid_grade = False
					while valid_grade != True:
						clrscr()
						print('\n PLEASE ENTER THE NEW VALID PROJECT GRADE MAX 100\n')
						choice = input("Your Answer: ")
						valid_grade = isValidGrade(choice)
					proj_grade = tryParseInt(choice)
					students[selected_id][2] = proj_grade
					clrscr()
					print('\n Student SUCCESSFULLY ADDED PRESS ENTER TO GO BACK\n')
					try:
						input("Press enter to continue")
					except SyntaxError:
						pass
					updateStudentGrades()
				elif clean_choice == 2:
					valid_grade = False
					while valid_grade != True:
						clrscr()
						print('\n PLEASE ENTER THE NEW VALID FINAL EXAM GRADE MAX 100\n')
						choice = input("Your Answer: ")
						valid_grade = isValidGrade(choice)
					final_grade = tryParseInt(choice)
					students[selected_id][3] = final_grade
					clrscr()
					print('\n Student SUCCESSFULLY ADDED PRESS ENTER TO GO BACK\n')
					try:
						input("Press enter to continue")
					except SyntaxError:
						pass
					updateStudentGrades()
				elif clean_choice == 3:
					showRootMenu()
				else:
					clrscr()
					print('\n INVALID INPUT\n')
					try:
						input("Press enter to continue")
					except SyntaxError:
						pass
					updateStudentGrades()
					
def viewStudentGrade():
	choice = 99
	while tryParseInt(choice) > 3:
		clrscr()
		print('\n PLEASE Select the type of Assesment\n')
		print(menu_obj.formatMenu(menu_obj.createMenu([7,8,9,10])))
		choice = input("\nYour Answer: ")

	if tryParseInt(choice) == 0:
		clrscr()
		print("\nSTUDENTS Discussion Forum Report Grade\n")
		x=0
		for each_student in students:
			print('Student ID: {} | Name: {} | DF Grade: {}'.format(x,each_student[0],each_student[1]))
			x += 1
		print ("\n[0] GO BACK\n")
		choice = input("Your Answer: ")
		if tryParseInt(choice) !=0:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewStudentGrade()
		else:
			viewStudentGrade()
	elif tryParseInt(choice) == 1:
		clrscr()
		print("\nSTUDENTS Project Grade\n")
		x=0
		for each_student in students:
			print('Student ID: {} | Name: {} | Project Grade: {}'.format(x,each_student[0],each_student[2]))
			x += 1
		print ("\n[0] GO BACK\n")
		choice = input("Your Answer: ")
		if tryParseInt(choice) !=0:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewStudentGrade()
		else:
			viewStudentGrade()
	elif tryParseInt(choice) == 2:
		clrscr()
		print("\nSTUDENTS Discussion Forum Report Grade\n")
		x=0
		for each_student in students:
			print('Student ID: {} | Name: {} | Final Exam Grade: {}'.format(x,each_student[0],each_student[3]))
			x += 1
		print ("\n[0] GO BACK\n")
		choice = input("Your Answer: ")
		if tryParseInt(choice) !=0:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewStudentGrade()
		else:
			viewStudentGrade()
	elif(tryParseInt(choice) == 3):
		showRootMenu()
	else:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewStudentGrade()

def viewLowGrades():
	choice = 99
	while tryParseInt(choice) > 3:
		clrscr()
		print('\n PLEASE Select the type of Assesment\n')
		print(menu_obj.formatMenu(menu_obj.createMenu([7,8,9,10])))
		choice = input("\nYour Answer: ")

	if tryParseInt(choice) == 0:
		clrscr()
		print("\nSTUDENTS With Below Average Discussion Forum Report Grade\n")
		ave_list = []
		for each_student in students:
			ave_list.append(each_student[1])
		df_ave = getAverage(ave_list)

		x=0
		for each_student in students:
			if each_student[1] < df_ave:
				print('Student ID: {} | Name: {} | DF Grade: {}'.format(x,each_student[0],each_student[1]))
			x += 1
		print ("\n[0] GO BACK\n")
		choice = input("Your Answer: ")
		if tryParseInt(choice) !=0:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewLowGrades()
		else:
			viewLowGrades()

	elif tryParseInt(choice) == 1:
		clrscr()
		print("\nSTUDENTS With Below Average Project Report Grade\n")
		ave_list = []
		for each_student in students:
			ave_list.append(each_student[2])
		proj_ave = getAverage(ave_list)

		x=0
		for each_student in students:
			if each_student[2] < proj_ave:
				print('Student ID: {} | Name: {} | Project Grade: {}'.format(x,each_student[0],each_student[2]))
			x += 1
		print ("\n[0] GO BACK\n")
		choice = input("Your Answer: ")
		if tryParseInt(choice) !=0:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewLowGrades()
		else:
			viewLowGrades()

	elif tryParseInt(choice) == 2:
		clrscr()
		print("\nSTUDENTS With Below Average Final Exam Report Grade\n")
		ave_list = []
		for each_student in students:
			ave_list.append(each_student[3])
		final_ave = getAverage(ave_list)

		x=0
		for each_student in students:
			if each_student[3] < final_ave:
				print('Student ID: {} | Name: {} | Final Exam Grade: {}'.format(x,each_student[0],each_student[3]))
			x += 1
		print ("\n[0] GO BACK\n")
		choice = input("Your Answer: ")
		if tryParseInt(choice) !=0:
			clrscr()
			print('\n INVALID INPUT\n')
			try:
				input("Press enter to continue")
			except SyntaxError:
				pass
			viewLowGrades()
		else:
			viewLowGrades()

	else:
		showRootMenu()

def viewTotalGrades():
	clrscr()

	print("A BAR CHART IS SHOWN AT ANOTHER WINDOW \n")

	print("PLEASE CLOSE THE CHART WINDOW TO EXIT \n")

	FONT_SIZE = 12
	FONT = ("Arial", FONT_SIZE, "normal")
	COLORS = ['#CC9933', '#6699CC', '#CC3399', '#996633', '#336699', '#0099CC', '#FF9999', '#CC0066', '#99CC00', '#CC3399', '#009933']

	data = {}

	for each_student in students:
		data[each_student[0]] = ((tryParseFloat(each_student[1]) * .20) + (tryParseFloat(each_student[2]) * .30) + (tryParseFloat(each_student[3]) * .50))
	print("Please Press Enter after A Graph have been shown")

	### Create and Setup the Window ###
	xmax = max(data.values())
	window = Screen()
	window.title("Total Report of Total Grades of Students for the Semester")
	height = 130 * (len(data) + 1)  # (the space between each bar is 30, the width of each bar is 100)
	window.setup(600, height)  # specify window size (width is 600)
	turtle = Turtle(visible=False)
	turtle.speed('fastest')
	turtle.penup()
	turtle.setpos(-225, -(height / 2) + 50)
	turtle.pendown()

	# draw x-axis and ticks
	xtick = 400 / 7

	for i in range(1, 8):
		turtle.forward(xtick)
		xv = float(xmax / 7 * i)
		turtle.write('%.1f' % xv, move=False, align="center", font=FONT)
		turtle.right(90)
		turtle.forward(10)
		turtle.backward(10)
		turtle.left(90)

	turtle.setpos(-225, -(height / 2) + 50)
	turtle.left(90)

	# draw bar and fill color
	pixel = xmax / 400
	recs = []  # bar height
	for value in data.values():
		recs.append(value / pixel)

	for i, rec in enumerate(recs):
		turtle.color('black')
		turtle.forward(30)
		turtle.right(90)
		turtle.begin_fill()
		turtle.forward(rec)
		turtle.left(90)
		turtle.forward(50 - FONT_SIZE/2)
		turtle.write('  ' + str(rec * pixel), move=False, align="left", font=FONT)
		turtle.forward(50 + FONT_SIZE/2)
		turtle.left(90)
		turtle.forward(rec)
		turtle.color(COLORS[i % len(COLORS)])
		turtle.end_fill()
		turtle.right(90)

	turtle.setpos(-225, -(height / 2) + 50)
	turtle.color('black')

	# draw y-axis and labels
	turtle.pendown()

	for key in data:
		turtle.forward(30)
		turtle.forward(10)
		turtle.write('  ' + key, move=False, align="left", font=FONT)
		turtle.forward(90)
	turtle.forward(30)
	### Tell the window to wait for the user to close it ###
	window.mainloop()
	
def viewTotalLowGrades():
	clrscr()
	print("BELOW Class Average Total Grades for the Semester\n")
	total_ave_list = []
	for each_student in students:
		total_ave_list.append((each_student[1] * .20) + (each_student[2] * .30) + (each_student[3] * .50))
	total_ave = getAverage(total_ave_list)

	x = 0
	for each_student in students:
		if ((each_student[1] * .20) + (each_student[2] * .30) + (each_student[3] * .50)) < total_ave:
			print('Student ID: {} | Name: {} | Total Semester Grade: {}'.format(x,each_student[0],((each_student[1] * .20) + (each_student[2] * .30) + (each_student[3] * .50))))
			x += 1

	print ("\n[0] GO BACK\n")
	choice = input("Your Answer: ")
	if tryParseInt(choice) !=0:
		clrscr()
		print('\n INVALID INPUT\n')
		try:
			input("Press enter to continue")
		except SyntaxError:
			pass
		finally:
			viewTotalLowGrades()
	else:
		showRootMenu()

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