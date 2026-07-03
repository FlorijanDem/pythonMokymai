def check_person_code(code):
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
    validation_number = int(code[10])
    
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

    if (remainder != 10):
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

print(check_person_code("46806013013"))