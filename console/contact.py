"""Author :Shamgar Musobero
		Purpose:To Add Contact In Your Computer 
		
	"""
# i declared the main because it does follows the order of the functions
def main():

	print("Welcome To Contact Management System")
	print("{}Add Contacts\n{}Search Contacts\n{}View Contacts\n{}Delete Contacts\n{}Exit".format(1,2,3,4,5))


	def goback():
		print(" * Main menu\n c Continue")
		ref =input("")
		# if the ref entered is not * or c then automatically it means it will continue to loop until the these 2 are entered
		while (ref== "*" or "c"):	
			if ref =="*":
				main()
			elif ref=="c":
				menu(num)
			else:
				print("Invalid Option")
			#calling the goback function
			goback()

	def view():
		file = open("example.txt","r")
		#printing the contents in the file
		for line in file.readlines():
			print(line)
	def entry():
		fo = open("example.txt", "a")
		#if the user enter name and surname and phonenumber 
		name = input("Enter your name:")
		surname= input("Enter your surname: ")
		phnmbr=input("Enter your phone number:")
				#printing the information to the file
		fo.writelines("\n{}-".format(name))
		fo.writelines("{}-".format(surname))
		fo.writelines("{}\n".format(str(phnmbr)))
	# Close opend file
		fo.close()
	def menu(num):
		if num == 1:
			print("Add Contacts")
			#opening the file called example
			
			try:
				#calling the the function of entry and goback
				entry()
				goback()
				#the error that we are catching
			except ValueError as e:
				#to the user we tell him to enter a number
				print("Enter A Number")
			
		elif num ==2:
			print("Search Contacts")

			fu = open("example.txt", "r")
			#asking the user for input
			search= input("Enter the contact that you want to search")
			
			#checking the search inputted in the file example
			if search in fu.read():
				print("The contact is there in the address")
			else:
				print("The contact is not  there in the address")
	
			goback()
		elif num== 3:
			print("View Contacts")
			# calling functions of view aand goback
			view()
			goback()
		elif num== 4:
			print("Delete Contacts")
			#enter the word you want to be deleted
			delete_word = input("Enter the contact you want to delete")
	
			with open('example.txt','r') as infile:
				newlist = [i for i in infile.read().split() if i!=delete_word]
				with open('example.txt','w') as outfile:
					#writing the others contents in the file
					outfile.write("\n".join(newlist[0:]))
					
			#calling the goback function	
			goback()
	
		elif num==5:
			print("Good Bye")
			##Exiting the program
			exit()
		else:
			#if the user enter the number that is different it outputs 
			print("Invalid Option")


#catching the error of the user of  not entering the integers
	try:
		#allow the user to enter the numbers
		num = int(input(""))
		menu(num)
#The error name is called ValueError
	except ValueError as e:
		print("Enter A Number")
		#calling the main function
		main()

if __name__ == "__main__": main()
