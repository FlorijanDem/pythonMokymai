line = "Zen trea Python, by Tim Peters"

x1 = line.split()
print(x1[1][-2])
print(x1[2][0])
print(x1[:1])
print(x1[-1]) 
print(x1[::-1])

for i in x1:
    print(i)

x2 = line.replace("Python", "Programming")
print(x2)