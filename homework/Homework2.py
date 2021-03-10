# CV APPLICATION
#Create 5 dictionaries. Each dictionary should represent a CV.
#Create a CV con the information of the 5 created people.


person_1 = {'name':'Delilah',
 'surname':'Wehner',
 'age':'23',
 'educationHistory':'Harvard University',
 'jobTitle':'Dynamic Operations Assistant',
 'EmployementHistory':'Lang LLC, Beier - Weissnat Inc.'}

person_2 = {'name':'Lisandro',
 'surname':'Hermiston',
 'age':'26',
 'educationHistory':'Oxford University',
 'jobTitle':'International Markets Engineer',
 'EmployementHistory':'Wilderman - Cruickshank, Dietrich LLC'}

person_3 = {'name':'Amiya',
 'surname':'Wolf',
 'age':'32',
 'educationHistory':'Stanford University',
 'jobTitle':'Chief Markets Developer',
 'EmployementHistory':'Yost - Wilderman Inc., Barrows - Schultz Group'}

person_4 = {'name':'Darrel',
 'surname':'Jenkins',
 'age':'37',
 'educationHistory':'Imperial Collage London',
 'jobTitle':'Central Solutions Consultant',
 'EmployementHistory':'Pfannerstill and Sons Group, Brekke, Breitenberg and Collier'}

person_5 = {'name':'Shakira',
 'surname':'Gislason',
 'age':'30',
 'educationHistory':'Georgia Tech. Uniniversity',
 'jobTitle':'Chief Functionality Planner',
 'EmployementHistory':'Collins LLC, Fisher and Smith Inc.'}

#Print the information on CVs created on the screen.
personList =[person_1, person_2, person_3, person_4, person_5]
for index in personList:
    print (f"Name: {index['name']},\n Surname: {index['surname']},\n Age: {index['age']},\n Edutacion History: {index['educationHistory']},\n JobTitle: {index['jobTitle']},\n Employement History: {index['EmployementHistory']}\n",end=" ")
    print("----------------------------------------------------------------")

