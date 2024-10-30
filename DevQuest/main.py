### Print a welcome message
print("Welcome to the DevQuest game!")
print("In this game, you will learn about some features of the Software Development Life Cycle!")
print("There are many different methods to the SDLC, so first, lets pick a method!")

### List of methods
methods = [
    "1. Scrum",
    "2. XP (Extreme Programming)",
    "3. Spotify Agile",
    "4. Kanban",
    "5. Lean"
]
print("Which methodology is calling your name?")
for m in methods:
    print(m)

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
    print("You have chosen Scrum how FUN! Lets get started with the sprint planning.")

def handXP():
    print("You have chosen XP, lets solve this mystery.")

def handle_spotify():
    print("You have chosen Spotify Agile! Let’s discuss squad autonomy.")

def handle_kanban():
    print("You have chosen Kanban! Time to manage your workflow.")

def handle_lean():
    print("You have chosen Lean! Let's focus on eliminating waste.")


### Check if the choice is valid
if methodChoice in methodDict:
    chosenMethod = methodDict[methodChoice]
    #eventually print response to each method pick
    print(f"How FUN! You have chosen: {chosenMethod}")
else:
    print("Invalid choice. Please select a number from 1 to 5.")
