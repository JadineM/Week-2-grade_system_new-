#Professional Practices Short Course – Candidate Assessment: 
#Title: Create a simple program to grade students based on their semesterly marks
#Author: Jadine Meghrajh
#Programming language: Python
#IDE: Sublime Text 2 & Python 3.10.2

#start

import csv 											 #importing a built in module to enable reading/manipulating/writing of csv files

inputfile = open('input.csv') 						 #tells the csv module to open the given "input.csv" file and assigns this file to an object (inputfile)
csv_inputfile = csv.reader(inputfile) 				 #pass the inputfile object to the csv module to create a csv file object
next(csv_inputfile)									 #tells the program to skip the first row as this data is not useful for further operation

header = ['Firstname', 'Surname','Average', 'Grade'] #assigning the headings that needs to be written to the new "output.csv" file

createfile = open('output.csv', 'w', newline="") 	 #open a new file for writing, with each information to be stored on the next line with no spaces
writer = csv.writer(createfile)						 #using the csv writer to write to the file

writer.writerow(header)						 		 #writes the respective header to the newly created "output.csv" file

for row in csv_inputfile:					 		 #iterate over the csv file object by looping over every row, using a for loop
	
	firstname = (row[0]) 					 		 #extracting the firstname in position 0 from the specific row as a string
	surname = (row[1]) 						 		 #extracting the surname in position 1 from the specific row as a string
	algebraperc = float(row[2]) 			 		 #extracting the algebra percentage in position 2 from the specific row and converting it to a float 
	calculusperc = float(row[3]) 			 		 #extracting the calculus percentage in position 3 from the specific row and converting it to a float 
	programmingperc = float(row[4]) 		 		 #extracting the programming percentage in position 4 from the specific row and converting it to a float 
	databasesperc = float(row[5]) 			 		 #extracting the databases percentage in position 5 from the specific row and converting it to a float 

	avrg = float(round(((algebraperc+calculusperc+programmingperc+databasesperc)/4),1)) 
	#calculating the average percentage per learner by using the total percentage divided by the number of subjects. Rounded off to 1 decimal as required 
	


	#the following if else function is used to calculate the learners symbol and thereafter write their details, average and symbol to a new csv file "output.csv"
	if( 80 <= avrg <= 100): 				   
		data = [firstname, surname, avrg, 'A'] 
		
	elif( 70 <= avrg <= 79.9):					
		data = [firstname, surname, avrg, 'B'] 
		
	elif( 60 <= avrg <= 69.9):
		data = [firstname, surname, avrg, 'C'] 

	elif( 50 <= avrg <= 59.9):
		data = [firstname, surname, avrg, 'D'] 
		
	elif( 40 <= avrg <= 49.9):
		data = [firstname, surname, avrg, 'E'] 

	else:
		data = [firstname, surname, avrg, 'F'] 
	
	writer.writerow(data)					  		 #write the respective data to the newly created "output.csv" file

inputfile.close() 							 		 #calling a method on the file object in order to close the file

#end