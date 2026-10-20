#Student score exercise
#Generates a class of people with different academic strength, each academic strength having their own probability weights for each scores. Average academic strength being the most dominant.
#Generated random grades for the subjects for each students based on their academic strength weights and stored it in a database.
#Created a few functions for interacting with it.
#Used dictionaries, tuple, lists, the random module and rich module.


#Importing necessary modules.
from rich import print
import random as rd
from rich.console import Console
from rich.panel import Panel

c = Console()

f_name = ["Hue", "Sahn", "Dhei", "Isah", "Behn", "Fhu", "Gah"]
l_name = ["Dhesan", "Elon", "Gahb", "Huio", "Palam", "Esahn", "Ghilan", "Thoam", "Shae" "Rhasa", "Dhat"]

subject = ("biology", "maths", "chemistry", "english", "physics")
#print(subject[0])


scores = [x for x in range(1, 11)]


#Score probability for different academic strength.
top = [0.55, 0.4, 0.04, 0.005, 0.003, 0.001, 0.0005, 0.0003, 0.00015, 0.00005]


ex = [0.25, 0.4, 0.3, 0.03, 0.01, 0.005, 0.002, 0.0015, 0.001, 0.0005]

good = [0.05, 0.1, 0.15, 0.2, 0.305, 0.1, 0.05, 0.03, 0.01, 0.005]

avg = [0.0025, 0.0225, 0.05 , 0.1, 0.325, 0.325, 0.1, 0.05, 0.0225, 0.0025]

fair = [x for x in reversed(good)]

low = [x for x in reversed(top)]


classPopulation = [0.003, 0.09, 0.2, 0.6, 0.1, 0.007]


studentType = {"top scorer": top, "excellent": ex, "good": good ,"average": avg, "fair": fair, "poor": low}
types = [i for i in studentType]




scoreList = {}
#Generates a person and their grades
for i in range(31):
    firstName = rd.choice(f_name)
    lastName = rd.choice(l_name)
    #Chooses their academic strength.
    type = rd.choices(types, classPopulation, k=1)[0]
    #Generates score based on academic strength.
    score = rd.choices(scores, reversed(studentType[type]), k=5)
    #Determine pass or fail status
    total = sum(score)
    status = "Passed" if total>=((len(subject)*10)/2) else "Failed"
    
    scoreList[i] = {"name": ' '.join([firstName, lastName]),
    "score": (dict((subject[i], score[i]) for i in range(len(subject)))), 
    "type": type,
    "status": status
    }


#Functions
def stats():
        """Displays the highest, lowest and mean scores for each subject."""
        stats = {}
        for i in subject:
            high = 0
            lowest = 10
            all = []
            for person in scoreList:
                p_scores = scoreList[person]["score"]
                s_score = p_scores[i]
                if s_score>high:
                    high = s_score
                if s_score<lowest:
                    lowest = s_score
                all.append(s_score)
            stats[i] = {"highest": high, "lowest": lowest, "mean": int(sum(all)/len(scoreList))}
        
        msg = ""     
        for i in stats:
            msg += f"{i.upper()}\n"   
            msg += f"Highest: {stats[i]['highest']}\n"
            msg += f"Lowest: {stats[i]['lowest']}\n"  
            msg += f"Mean: {stats[i]['mean']}\n\n"
        print("")
        c.print(Panel(msg, border_style="cyan", title = "Statistics"))
              
                    
                
        
def show():     
    """Displays a list of the students in the class and their grades."""                   
    for u, y in scoreList.items():
        print("\n", y["name"].upper(), y["type"].title())
        print(f" Status: {y['status']}")
        for i in y["score"]:
            score = y["score"][i]
            #Color coding grades.
            color = "white"
            if score<=3:
                color = "red"
            elif score>=4 and score<=7:
                color = "yellow"
            elif score>7:
                color = "green"
            print(f" {i.title()}: [{color}]{y['score'][i]}[/{color}]")
        print(f"Total: {sum(y['score'].values())}")



def top():
    """Prints the names of the students who got the highest score and their score."""
    highscore = 0
    person = []
    for i in scoreList:
        student = scoreList[i]
        studentScore = sum(student['score'].values())
        if studentScore >= highscore:
            if studentScore == highscore:
                person.append(i)
            else:
                person = []
                person.append(i)
            highscore = studentScore
    people=""                
    for i in person:
        people += f" {scoreList[i]['name']}," 
    people = people[:-1]    
    people.strip()      
    msg = f"Name: {people.title()}\nScore: {highscore}/{len(subject)*10}"
    p = Panel(msg, title="Top Scorer")
    c.print(p)




def view(student):
    """Returns the grades of the student it takes as an argument."""
    
    student = student.strip().lower()
    for i in scoreList:
        if scoreList[i]['name'].lower().strip() == student:
            studentObj = scoreList[i]
            msg = ""     
            msg += f"Academic Strength: {studentObj['type']}\n"     
            msg += f"Status: {studentObj['status']}\n"   
            for sub in studentObj['score']:
                score = studentObj['score'][sub]
                #Color coding grades.
                color = "white"
                if score<=3:
                    color = "red"
                elif score>=4 and score<=7:
                    color = "yellow"
                elif score>7:
                    color = "green"  
                msg += f"{sub.title()}: [{color}]{score}[/{color}]\n"     
            msg += f"Total: {sum(studentObj['score'].values())}/{len(subject)*10}"    
            p = Panel(msg, title = studentObj['name'])    
            return p
    return "No such person found."                           
                        

def main():
    """Main function that runs."""
    running = True
    while running:
        print("\n______Student Score______")    
        print("1. View Class list with scores") 
        print("2. View Individual student with their score")
        print("3. View the top scorer")
        print("4. View the statistics for each subject")
        print("5. Exit")
        try:
            action = int(input("Enter number corresponding to the action you'd like to perform: "))
        except:
            print("Invalid input, must be a number.")
            continue
        
        match action:
            case 1:
                show()
                continue
            case 2:
                person = input("Name: ")
                msg = view(person)
                c.print(msg)
                continue
            case 3:
                top()
                continue
            case 4:
                stats()
                continue
            case 5:
                running = False
                continue
        print("Invalid action.")
        
main()                                      