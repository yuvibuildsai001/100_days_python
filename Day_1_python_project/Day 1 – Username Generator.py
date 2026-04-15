import re

print("### USERNAME GENERATOR ###")

# function to clean name (remove special chars & spaces)
def clean_name(name):
    return re.sub(r'[^a-zA-Z]', '', name)

# input namesfg
while True:
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()

    first_name = clean_name(first_name)
    last_name = clean_name(last_name)

    if first_name and last_name:
        break
    else:
        print("❌ Names must contain only letters and not be empty.")

# birth year validation
while True:
    year_of_birth = input("Enter birth year: ").strip()

    if year_of_birth.isdigit():
        year = int(year_of_birth)
        if 1900 <= year <= 2026:
            break
        else:
            print("❌ Enter a realistic year (1900–2026).")
    else:
        print("❌ Numbers only!")

# formatting
first_name = first_name.capitalize()
last_name = last_name.capitalize()

print("\n### Generated Usernames ###\n")

print(f"1 -> {first_name}{last_name}{year}@xyz.com")
print(f"2 -> {first_name[0]}{last_name}{year}@xyz.com")
print(f"3 -> {first_name}{year}@xyz.com")