def check_person_code(code, have_validation_code = True):
    first_number = int(code[0])
    second_number = int(code[1])
    st3_number = int(code[2])
    st4_number = int(code[3])
    st5_number = int(code[4])
    st6_number = int(code[5])
    st7_number = int(code[6])
    st8_number = int(code[7])
    st9_number = int(code[8])
    st10_number = int(code[9])
    
    if(have_validation_code == True):
        validation_number = int(code[10])
    elif(have_validation_code == False):
        validation_number:int

    if first_number < 0 or first_number > 6:
        return False
    
    sum = 0
    sum += first_number * 1
    sum += second_number * 2
    sum += st3_number * 3
    sum += st4_number * 4
    sum += st5_number * 5
    sum += st6_number * 6
    sum += st7_number * 7
    sum += st8_number * 8
    sum += st9_number * 9
    sum += st10_number * 1

    remainder = sum % 11

    if (have_validation_code == False and remainder != 10):
        return remainder
    elif (remainder != 10):
        if (remainder == validation_number):
            return True
        
    elif (remainder == 10):
        sum = 0
        sum += first_number * 10
        sum += second_number * 9
        sum += st3_number * 8
        sum += st4_number * 7
        sum += st5_number * 6
        sum += st6_number * 5
        sum += st7_number * 4
        sum += st8_number * 3
        sum += st9_number * 2
        sum += st10_number * 1
        
        reversed_remainder = sum % 11
        if (reversed_remainder == remainder):
            return True
    else:
        return False

# print(check_person_code("46806013013"))

def generate_person_code(gender, birth_date, line):
    
    date_split = birth_date.split("-")
    first_number:int
    print(int(date_split[0]))

    if int(date_split[0]) >= 1801 and int(date_split[0]) < 1900:
        if gender == "male":
            first_number = 1
        elif gender == "woman":
            first_number = 2
    elif int(date_split[0]) >= 1901 and int(date_split[0]) < 2000:
        if gender == "male":
            first_number = 3
        elif gender == "woman":
            first_number = 4
    elif int(date_split[0]) >= 2001 and int(date_split[0]) < 2100:
        if gender == "male":
            first_number = 5
        elif gender == "woman":
            first_number = 6
    else:
        return "Wrong date range"
    
    second_number = int(date_split[0][2])
    st3_number = int(date_split[0][3])
    st4_number = int(date_split[1][0])
    st5_number = int(date_split[1][1])
    st6_number = int(date_split[2][0])
    st7_number = int(date_split[2][1])
    st8_number = int(line[0])
    st9_number = int(line[1])
    st10_number = int(line[2])
    
    persona_code_without_validation = f"{first_number}{second_number}{st3_number}{st4_number}{st5_number}{st6_number}{st7_number}{st8_number}{st9_number}{st10_number}"
    validation_number = check_person_code(code = persona_code_without_validation, have_validation_code = False)
    persona_code_final = f"{persona_code_without_validation}{validation_number}"

    return persona_code_final

print(generate_person_code(gender = "male", birth_date = "2020-01-01", line = "300"))