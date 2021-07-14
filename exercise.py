'''
Given the current year and the year of birth provided by the user calculate and return the age of the user.
'''

def calculateAgeofAnIndividual(Currentyear, yearOfBirth):
    age = Currentyear - yearOfBirth
    return age

def userCalculateAgeOfAnIndividual():
    currentyear = int(input("Enter the current year"))    
    yearOfBirth = int(input("Enter the year of birth"))
    return calculateAgeofAnIndividual(currentyear, yearOfBirth)

print (userCalculateAgeOfAnIndividual())



