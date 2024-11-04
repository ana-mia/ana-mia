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
    print_d("You have chosen Scrum!")
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
    print_d("Roles in Scrum include:\n- **Scrum Master:** Facilitates the process and resolves impediments.\n- **Product Owner:** Represents the stakeholders and prioritizes the backlog.\n- **Development Team:** A cross-functional team that delivers the product increments.")
    time.sleep(2)
    
    print_d("Your coding task: Implement a simple to-do list feature where users can add, remove, and view tasks.")
    

def handleXP():
    print_d("You have chosen XP (Extreme Programming)!")
    time.sleep(1)
    print("Overview: XP is an agile software development framework that emphasizes technical excellence and frequent releases.")
    time.sleep(2)
    print("**Strengths:**\n- Encourages feedback and adaptability\n- Focuses on high-quality code\n- Engages customers frequently")
    time.sleep(2)
    print("**Weaknesses:**\n- Can be challenging to implement without a strong team\n- Requires strong discipline and commitment")
    time.sleep(2)
    print("**History:**\n- Introduced by Kent Beck in the late 1990s.")
    time.sleep(2)
    
    print_d("Roles in XP include:\n- **Coach:** Guides the team in XP practices.\n- **Customer:** Provides requirements and feedback.\n- **Developers:** Write the code and work closely with the customer.")
    time.sleep(2)
    
    print_d("Your coding task: Create a simple unit test suite for a calculator application.")
    

def handleSpotify():
    print_d("You have chosen Spotify Agile!")
    time.sleep(1)
    print("Overview: This model promotes autonomy and alignment among teams (squads) while maintaining a cohesive vision.")
    time.sleep(2)
    print("**Strengths:**\n- Fosters team ownership\n- Supports innovation and experimentation\n- Balances autonomy with coordination")
    time.sleep(2)
    print("**Weaknesses:**\n- May lead to silos if not managed well\n- Requires strong leadership for alignment")
    time.sleep(2)
    print("**History:**\n- Developed by Spotify, the model gained popularity for its unique team structure.")
    time.sleep(2)
    
    print_d("Roles in Spotify Agile include:\n- **Squad Lead:** Oversees the squad and aligns with company goals.\n- **Product Owner:** Manages the backlog and prioritizes tasks.\n- **Chapter Lead:** Ensures skill development within specific areas.")
    time.sleep(2)
    
    print_d("Your coding task: Build a feature that allows users to create and manage playlists in a music application.")
    

def handleKanban():
    print_d("You have chosen Kanban!")
    time.sleep(1)
    print("Overview: Kanban focuses on visualizing work, limiting work in progress, and optimizing flow.")
    time.sleep(2)
    print("**Strengths:**\n- Promotes visibility of work\n- Helps identify bottlenecks\n- Flexible and easy to implement")
    time.sleep(2)
    print("**Weaknesses:**\n- Can be less structured than other methodologies\n- Requires continuous monitoring")
    time.sleep(2)
    print("**History:**\n- Originated in manufacturing, developed by Taiichi Ohno at Toyota.")
    time.sleep(2)
    
    print_d("Roles in Kanban include:\n- **Service Delivery Manager:** Ensures that the team delivers value.\n- **Team Members:** Responsible for completing tasks and managing their workflow.")
    time.sleep(2)
    
    print_d("Your coding task: Create a Kanban board where tasks can be moved between different stages (To Do, In Progress, Done).")


def handleLean():
    print_d("You have chosen Lean!")
    time.sleep(1)
    print("Overview: Lean software development focuses on optimizing efficiency and eliminating waste.")
    time.sleep(2)
    print("**Strengths:**\n- Increases efficiency\n- Reduces waste\n- Promotes continuous improvement")
    time.sleep(2)
    print("**Weaknesses:**\n- May require a culture shift\n- Can be misunderstood as a cost-cutting measure")
    time.sleep(2)
    print("**History:**\n- Inspired by Lean manufacturing principles.")
    time.sleep(2)
    
    print_d("Roles in Lean include:\n- **Lean Leader:** Guides the team towards efficiency.\n- **Team Members:** Contribute to process improvement and efficiency.")
    time.sleep(2)
    
    print_d("Your coding task: Develop a feature that tracks and visualizes process efficiency over time.")



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