
import sys

def initial():
	r, c = int(input("Initial Number of Books in the Library = ")), 6
	
	b = []
	print(b)
	for i in range(r):
		print("\nEnter Book %d Details in the Following Order (ONLY):" % (i+1))
		print(" NOTE: the * Indicates Mandatory Fields")
		print("-----------------------------------------------------------------------------------------")
		temp = []
		for j in range(c):
		
			if j == 0:
				temp.append(str(input("Enter Name of the Book *: ")))
				
				
				if temp[j] == '' or temp[j] == ' ':
					sys.exit(
						"Name is a mandatory field. Process exiting due to blank field...")
					
					
			if j == 1:
				temp.append(int(input("Enter Book ID *: ")))
				
			if j == 2:
				temp.append(str(input("Enter Name of the Author : ")))
				
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None
					
			if j == 3:
				temp.append(int(input("Enter Price of the Book (in ₹ ) : ")))
				
				
			if j == 4:
				temp.append(
					int(input("Enter Quantity of the Book : ")))
			
				
				
					
		b.append(temp)
		
	
	print(b)
	return b

def menu():
	print("********************************************************************")
	print("\t\t\t LIBRARY  MANAGEMENT  SYSTEM  [LMS]", flush=False)
	print("********************************************************************")
	print("\t Welcome to LMS \n")
	print("1. Insert Record of New Book ")
	print("2. Delete All Records ")
	print("3. Search For a Particular Book Record ")
	print("4. Display All Book Records")
	print("5. Exit ")

	
	ch = int(input("Please enter your choice: "))
	
	return ch

def insert(br):
	
	d = []
	for i in range(len(br[0])):
		if i == 0:
			d.append(str(input("Enter Name of the Book : ")))
		if i == 1:
			d.append(int(input("Enter Book ID : ")))
		if i == 2:
			d.append(str(input("Enter Author of the Book : ")))
		if i == 3:
			d.append(int(input("Enter Price of the Book : ")))
		if i == 4:
			d.append(
				int(input("Enter Quantity of the Book : ")))
	br.append(d)
	
	return br


def deleteall(br):
	
	return br.clear()

def search(br):
	
	ch = int(input("Enter Search Criteria \n\
	1. Book Name\n2. Book ID \n3. Name of the Author \n4. Price \n5. Quantity \
	\nPlease enter (from 1-5): "))
	
	
	temp = []
	check = -1
	
	if ch == 1:
	
		query = str(
			input("Please Enter the Name of the Book You Wish to Search : "))
		for i in range(len(br)):
			if query == br[i][0]:
				check = i
				temp.append(br[i])
				
	elif ch == 2:
	
		query = int(
			input("Please Enter the Book ID : "))
		for i in range(len(br)):
			if query == br[i][1]:
				check = i
				temp.append(br[i])
				
	elif ch == 3:
	
		query = str(input("Please Enter the Name of the Author : "))
		for i in range(len(br)):
			if query == br[i][2]:
				check = i
				temp.append(br[i])
				
	elif ch == 4:
	
		query = int(input("Please Enter the Price : "))
		for i in range(len(br)):
			if query == br[i][3]:
				check = i
				temp.append(br[i])
				
	elif ch == 5:
	
		query = int(
			input("Please enter the Quantity at Hand :  "))
		for i in range(len(br)):
			if query == br[i][4]:
				check = i
				temp.append(br[i])
		
		
	else:
	
		print("Invalid Search Criteria !!! ")
		return -1
	
	
	if check == -1:
		return -1
		
	else:
		display(temp)
		return check
		


def display(br):
	if not br:
	
		print("List is Empty: []")
	else:
		for i in range(len(br)):
			print(br[i])

def exitall():

	print("********************************************************************")
	print("Thank You for Choosing LMS.")
	print("Please Visit Again!")
	print("********************************************************************")
	sys.exit("Goodbye!!!!")

# Main function code
print("....................................................................")
print("Hello All, Welcome to Library Management System ")
print("....................................................................")

ch = 1
br = initial()
while ch in (1, 2, 3, 4, 5):
	ch = menu()
	if ch == 1:
		br = insert(br)
	elif ch == 2:
		br = deleteall(br)
	elif ch == 3:
		d = search(br)
		if d == -1:
			print("The Record Does Not Exist. Please Try Again")
	elif ch == 4:
		br = display(br)
	else:
		exitall()

