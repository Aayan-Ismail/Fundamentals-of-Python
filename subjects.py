import random

subject = ["English" , "Maths" , "Geography" , "Latin" , "German" , "French" , "Irish" , "History" , "P.E" , "Religion" , "CSPE" , "Art"]
number = random.randint(2,10)
value = random.choice(subject)

favourite_subject = "{0} is my favourite subject. {1} hours is sufficent to study {0}" .format(value, number)

print(favourite_subject)