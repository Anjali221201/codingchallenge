# #  Day 12: Inheritance
# Objective
# Today, we’re delving into Inheritance. 

# Task
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# A Student class constructor, which has 4 parameters:
# A string, firstName.
# A string, lastName.
# An integer, idNumber.
# An integer array (or vector) of test scores, scores.
# A char calculate() method that calculates a Student object’s average and returns the grade character representative of their calculated average:
# Input Format
# The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.

# The first line contains firstname, lastName, and idNumber, separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes scores.

# Constraints
# 1 <= length of firstName, length of lastName <= 10
# length of idNumber = 7
# 0 <= score <= 100
# Output Format
# Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

# Sample Input

# Heraldo Memelli 8135627
# 2
# 100 80
# Sample Output

#  Name: Memelli, Heraldo
#  ID: 8135627
#  Grade: O
# Explanation

# This student had 2 scores to average: 100 and 80. The student’s average grade is (100 + 800) / 2 = 90. An average grade of 90 corresponds to the letter grade O, so the calculate() method should return the character'O'.
#solution:-
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, first_name, last_name, id, scores):
        super().__init__(first_name, last_name, id)
        self.test_scores = scores
    def calculate(self):
        total = sum(self.test_scores)
        avg = total // len(self.test_scores)

        if avg >= 90 and avg <= 100:
            return 'O'
        elif avg >= 80 and avg < 90:
            return 'E'
        elif avg >= 70 and avg < 80:
            return 'A'
        elif avg >= 55 and avg < 70:
            return 'P'
        elif avg >= 40 and avg < 55:
            return 'D'
        else:
            return 'T'



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())