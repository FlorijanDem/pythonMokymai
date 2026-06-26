data = {"Jonas" : [9, 7], "Vasia" : [8, 7]}

print(data)
# addNewStudentName = input()
# print(addNewStudentName)

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
        data[x] = []
    elif command == "addGrade":
        print("Enter student")
        x = input()
        print("Enter grade")
        grade = int(input())
        data[x].append(grade)
    elif command == "avgByStudent":
        print("Enter student name")
        x = input()
        grades = data[x]
        avg = sum(grades) / len(grades)
        print(f"Average is {avg}")
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