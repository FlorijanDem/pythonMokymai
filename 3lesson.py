# Sukurkite klasę studentas, su sąvybėmis vardas, pavardė ir pazymiai.
 
# Sukurkiet bent tris objektus iš šios klasės. PRidėkite jiems bent po tris pazymius kiekvienam.
 
# Parašykite metodą, kuris paskaičiuotų šių studentų vidurkį. 
 
# Sudėkite šiuos objektus į sąrašą ir parašykite funkcija kuri paskaičiuotų iš šio sąrašo, kurio studento vidurkis yra didžiausias, turėtų ir išvesti:
 
# Jono Jonaičio vidurkis 8.7 yra didžiausias

class Student:
    def __init__(self, first_name, last_name, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = marks

    def marks_avg(self):
        avg:float = 0
        sum:int = 0
        for i in self.marks:
            sum = sum + i
        avg = sum / len(self.marks)
        return avg
    
    

first = Student("Jonas", "Jonaitis", [10, 10, 9])
second = Student("Agne", "Agnaite", [8, 9, 9])
theerd = Student("Dobilas", "Dobilaitis", [1, 9, 10])


student_list = [first, second, theerd]
def best_avg(data):
    avg_values = []
    for i in data:
        avg_values.append(i.marks_avg())

    best = max(avg_values)
    index_of_best = avg_values.index(best)
    best_student = data[index_of_best]

    result = f"{best_student.first_name} {best_student.last_name} {best:.1f} yra didziausias"
    return result
    

print(best_avg(student_list))