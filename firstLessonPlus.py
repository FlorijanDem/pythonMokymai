data = {"Jonas" : [9, 7], "Vasia" : [8, 7]}

print(data)

class checkStudendInList:
    def __init__(self, students):
        self.students = students

    def exists(self, name):
        return name in self.students

    def haveGrades(self, name):
        return len(self.students[name]) > 0
    
checker = checkStudendInList(data)

def inRange(number):
    if 1 <= number <= 10:
        return True
    else:
        return False
        

def process_command(command):
    if command == "help":
        print ("addStudent to add student")
    
    elif command == "list":
        for i in data:
            print(i)
            print(data[i])
    
    elif command == "addStudent":
        print("Enter student name")
        x = input()
        if checker.exists(x) == True:
            print("This student already exists")
        else:
            data[x] = []
    
    elif command == "addGrade":
        print("Enter student")
        x = input()
        if checker.exists(x) == True:
            print("Enter grade")
            grade = int(input())
            if inRange(grade) == True:    
                data[x].append(grade)
            else:
                print("Wrong range")
        else:
            print("Student do not exists")
    
    elif command == "avgByStudent":
        print("Enter student name")
        x = input()
        if checker.exists(x) == True:
            if checker.haveGrades(x) == True:
                grades = data[x]
                avg = sum(grades) / len(grades)
                print(f"Average is {avg}")
            else:
                print("Student did not have grades")
        else:
            print("This student do not exists")
    
    elif command == "theBestStudent":
        best_name = None
        biggest = 0
        for name, grades in data.items():
            avg = sum(grades) / len(grades)

            if best_name is None or avg > biggest:
                biggest = avg
                best_name = name

        print(f"{best_name} has the biggest average grade: {biggest}")
    
    elif command == "deleteStudent":
        print("Enter student name")
        x = input()
        data.pop(x)

    elif command == "exit":
        print("Exit from app")
        return False
    else:
        print("Unknown command")

while True:
    command = input(">")

    if process_command(command) == False:
        break