import random

from pyfiglet import figlet_format
from colorama import Fore, Style

title = figlet_format("TRIPLE - X - PRISION ", font="small")

print(Fore.RED + title + Style.RESET_ALL)

level = 1
attempt = 3
print("YOU ARE IN THE JAIL.... IN THIS JAIL 5 DOORS AND EACH DOOR IS PROCTED BY PIN LOCK...🔏 \nYOU HAVE TO BREAK ALL THE LOCK 🔓\nAND YOU HAVE ONLY 3 ATTEMPTS")
print("""
   ╔═══════════════════════════╗
   ║ ||  ||  ||  ||  ||  ||  ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ║                           ║
   ║         ( •_• )           ║
   ║         /|   |\\          ║
   ║         /     \\          ║
   ║      PRISONER LOCKED      ║
   ║                           ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ╚═══════════════════════════╝
""")

while level <= 5:
    print(f"\nLEVEL = ",level)

    num1 = random.randint(1,5)
    num2 = random.randint(1,5)
    num3 = random.randint(1,5)

    total = num1 + num2 + num3
    product = num1 * num2 * num3

    print("There are 3 number in Code".upper())
    print(">> sum of Numbers :".upper(), total)
    print(">> Product Of Numbers:".upper(), product)
    print()

    user_input = input("Guess the password: ".upper()).split()
    print()

    # 🔹 check length
    while len(user_input) != 3:
        user_input = input("Please enter 3 Digits: ".upper()).split()
        print()

    # 🔹 check digits
    while not all(i.isdigit() for i in user_input):
        user_input = input("Please Enter only Integer: ".upper()).split()
        print()

    # 🔹 check answer
    if (int(user_input[0]) + int(user_input[1]) + int(user_input[2]) == total and
        int(user_input[0]) * int(user_input[1]) * int(user_input[2]) == product):

        print(">> PASSWORD CRACKED SUCCESSFULLY ✔️ \n".upper())
        level += 1
        attempt = 3
        if level > 5:
          print("""
   ╔═══════════════════════════╗
   ║ ||  ||  ||  ||  ||  ||  ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ║                           
   ║      CODE CRACKED!        
   ║     YOU ARE FREE 🔓       
   ║                           ║
   ╚═══════════════════════════╝

            ( •̀ᴗ•́ )
            /|   |\\
            /     \\
        🏃 YOU ESCAPED!
""")
          print("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝

        🎉 YOU WIN THE GAME 🎉
""")

    else:
        print("wrong Password!❌ Please Try Again\n".upper())
        attempt -= 1
        print(f"You have {attempt} Attempt left\n".upper())

        if attempt == 0:
            print(Fore.RED + "💀 GAME OVER\n" + Style.RESET_ALL)
            print(Fore.YELLOW + "You are permanently locked in the jail!".upper() + Style.RESET_ALL)
            print("""
   ╔═══════════════════════════╗
   ║ ||  ||  ||  ||  ||  ||  ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ║                           ║
   ║         ( x_x )           ║
   ║         /|   |\\          ║
   ║         /     \\          ║
   ║       GAME OVER...        ║
   ║     YOU ARE LOCKED 🔒     ║
   ║                           ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ║ ||  ||  ||  ||  ||  ||  ║
   ╚═══════════════════════════╝
""")
            break
