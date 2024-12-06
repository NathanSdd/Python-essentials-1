#Student: Nathan Santos de Deus
#Email: nathandosantos@hotmail.com
#Student Number: 77304



#Introducion message
def menu():
    print(48*"=" + "\nWelcome to the Blood Type Compatibility Checker!\n" + 48*"=" +"\n")
    print("Please choose an option to continue:\n")
    print("1. Check who can donate to your blood type.")
    print("2. Check who you can donate blood to.")
    print("3. Exit the program.")



#Dictionary to save blood type information and compatibility
blood_type_compatibility = {
    "A+": {"gives": ["A+", "AB+"],
           "receives": ["A+", "A-", "O+", "O-"]},
    
    "O+": {"gives": ["O+", "A+", "B+", "AB+"],
           "receives": ["O+", "O-"]},

    "B+": {"gives": ["B+", "AB+"],
           "receives": ["B+", "B-", "O+", "O-"]},

    "AB+": {"gives": ["AB+"],
            "receives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]},

    "A-": {"gives": ["A+", "A-", "AB+", "AB-"],
           "receives": ["A-", "O-"]},

    "O-": {"gives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
           "receives": ["O-"]},

    "B-": {"gives": ["B+", "B-", "AB+", "AB-"],
           "receives": ["B-", "O-"]},

    "AB-": {"gives": ["AB+", "AB-"],
            "receives": ["AB-", "A-", "B-", "O-"]}
}


#Function to check validity of the given blood type
def blood_type_validation (blood):
    if blood in blood_type_compatibility:
        return True
    else:
        print(f"Invalid blood type: {blood}. Please enter a valid blood type.")
        return False



#Funtion to check validity of the menu options
def menu_type_validation (menu_choice):
    if menu_choice in ["1", "2", "3"]:
        return True
    else:
        print(f"Invalid menu choice. Please enter 1, 2 or 3.")
        return False
    


#functions to bring gives and receives blood type from blood_type_compatibility
def gives_to (blood):
    return blood_type_compatibility [blood]["gives"]

def receives_from (blood):
    return blood_type_compatibility [blood]["receives"]



#Function to run the program
def program():
    while True:
        menu()
        menu_choice = input("Enter your choice (1, 2 or 3): ").strip()

        if not menu_type_validation(menu_choice): 
            continue

        if menu_choice == "3":
            print ("Thank you for using the Blood Type Compatibility Checker.\nGoodbye!")
            break

        blood = input ("Enter your blood type (e.g., A+, O-, AB+): ").upper()

        if not blood_type_validation(blood):
            continue

        if menu_choice == "1":
            gives = gives_to (blood)
            print (f"Blood type {blood} can donate to {gives}")

        if menu_choice == "2":
            receives = receives_from (blood)
            print (f"Blood type {blood} can receive donation from: {receives}")


program()

            