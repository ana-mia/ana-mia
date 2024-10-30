import time

def print_d(text, delay=0.05):
    for letter in text:
        print(letter, end='', flush=True)  # Print each word followed by a space
        time.sleep(delay)  # Pause for the specified delay
    print()  # Move to the next line after finishing

### Print a welcome message
print_d("Welcome to the DevQuest game!")
time.sleep(2)
print_d("In this game, you will learn about some features of the Software Development Life Cycle!")
time.sleep(2)
print_d("Lets review what the Software Development Life Cycle is and why it is so important")
print("\n")
time.sleep(2)

def printSdlcOverview():
    print_d("The Software Development Life Cycle (SDLC) is a structured process used for developing software.")
    print_d("It outlines the steps that teams follow to plan, create, test, and deploy software applications.")
    print("\n")
    print_d("The key phases of SDLC include:")
    print_d("1. **Planning:** Identifying project goals, scope, and resources needed.")
    print_d("2. **Analysis:** Gathering requirements and analyzing the needs of the stakeholders.")
    print_d("3. **Design:** Creating architecture and design specifications for the software.")
    print_d("4. **Development:** Writing the actual code to build the software application.")
    print_d("5. **Testing:** Verifying that the software meets requirements and is free of bugs.")
    print_d("6. **Deployment:** Releasing the software to users and providing ongoing support.")
    print_d("7. **Maintenance:** Performing updates, bug fixes, and enhancements after deployment.")
    print("\n")
    print_d("The SDLC is important because it provides a systematic approach to software development, ensuring quality and efficiency.")

printSdlcOverview()

print_d("There are many different methods to the SDLC, so first, lets pick a method!")
time.sleep(3)

### List of methods
methods = [
    "1. Scrum",
    "2. XP (Extreme Programming)",
    "3. Spotify Agile",
    "4. Kanban",
    "5. Lean"
]
print("\n")

for m in methods:
    print(m)

time.sleep(1)
print_d("Which methodology is calling your name? Pick carefully! When you're ready enter your choice below")

### Prompt user for a chioce
methodChoice = input("> ")

### Validate user input and map to name
methodDict = {
    "1": "Scrum",
    "2": "XP (Extreme Programming)",
    "3": "Spotify Agile",
    "4": "Kanban",
    "5": "Lean"
}

def handleScrum():
    print("You have chosen Scrum!")
    time.sleep(1)
    print("Overview: Scrum is an agile framework for managing complex projects. It emphasizes teamwork, accountability, and iterative progress.")
    time.sleep(2)
    print("**Strengths:**\n- Promotes team collaboration\n- Provides flexibility\n- Delivers working software frequently")
    time.sleep(2)
    print("**Weaknesses:**\n- Requires commitment from the team\n- Can be misapplied if not understood well")
    time.sleep(2)
    print("**History:**\n- Created in the early 1990s by Ken Schwaber and Jeff Sutherland.")
    time.sleep(2)

    ## Now give the player a real world example
    

def handleXP():
    print("You have chosen the XP!")

    ## Now give the player a real world example

def handleSpotify():
    print("You have chosen Spotify Agile!")

    ## Now give the player a real world example

def handleKanban():
    print("You have chosen Kanban!")

    ## Now give the player a real world example

def handleLean():
    print("You have chosen Lean!")

    ## Now give the player a real world example


### Check if the choice is valid
if methodChoice in methodDict:
    chosenMethod = methodDict[methodChoice]
    if methodChoice == "1":
        time.sleep(1)
        handleScrum()
    elif methodChoice == "2":
        time.sleep(1)
        handleXP()
    elif methodChoice == "3":
        time.sleep(1)
        handleSpotify()
    elif methodChoice == "4":
        time.sleep(1)
        handleKanban()
    elif methodChoice == "5":
        time.sleep(1)
        handleLean()

else:
    print("Invalid choice. Please select a number from 1 to 5.")