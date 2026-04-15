from pyfiglet import figlet_format
from colorama import Fore

print(Fore.LIGHTGREEN_EX + figlet_format("Welcome  To\nMovie Ticket Checker").upper())

bill = 0

movies = ["1. Dhurander","2. Dhurander-2","3. Toxic" ]
for movie in movies:
    print(movie)

choose_movie = int(input("Please choose a movie by Numbers :"))

price_by_age = """
Child (<12) → ₹100
Teen (12–18) → ₹150
Adult (18–60) → ₹200
Senior (>60) → ₹120
"""
print(price_by_age)
user_age = int(input("Please enter your Age :"))

if user_age <12:
    bill += 100
elif user_age >=12 and user_age < 18:
    bill += 150
elif user_age >= 18 and user_age < 60:
    bill += 200
elif user_age >=60:
    bill += 120

print(bill)