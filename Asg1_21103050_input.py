#Question 1

i= int(input('Enter the value of i:')) #first value by user
j = int(input('Enter the value of j:'))#second value by user
k = int(input('Enter the value of k:'))#third value by user

avg= float((i+j+k)/3)#average of three numbers

print('The average of the given numbers = ', avg)

#Question 2

i= float(input('Please enter your gross income to the nearest penny '))
j = int(input('Please enter the number of dependents '))

taxable_income = float(i-10000-(3000*j))

tax = float(taxable_income*0.2)
print('Total Payable Tax = ', tax) #the tax paid 

#Question 3

sid = input('Please enter your Student ID: ')
name = input('Please enter your name: ')
gender = input('Gender : M/F/U ')
branch = input('Please enter your branch name: ')
cgpa = input('Please enter your cgpa ')

L = [sid, name, gender, branch, cgpa] #details of the student

print(L)

#Question 4 

std1 = int(input('Student 1: '))
std2 = int(input('Student 2: '))
std3 = int(input('Student 3: '))
std4 = int(input('Student 4: '))
std5 = int(input('Student 5: '))
#input taken from user
L = [std1, std2, std3, std4, std5]

print('List of marks of the students: ',L)

L.sort()

print('List of marks of the students in the ascending order: ',L) #marks in ascending order

L.sort(reverse = True)

print('List of marks of the students in the descending order: ',L) #marks in descending order

#Question 5(a)

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

del list[3]

print(list)

#Question 5(b)

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list[3:5] = ['purple']

print(list)