# def calculate_life_path_number(birth_date):
#     month, day, year = birth_date.split('/')
#     month = int(month)
#     day = int(day)
#     year = int(year)

#     total = month + day + year
#     while total > 9:
#         total = sum(int(digit) for digit in str(total))

#     return total
def calculate_life_path_number(birthdate_parts):
    # Calculate the life path number
    life_path_number = sum(int(part) for part in birthdate_parts)
    
    # Reduce the sum to a single digit unless it's a master number
    while life_path_number > 9:
        digits = [int(d) for d in str(life_path_number)]
        life_path_number = sum(digits)
    
    return life_path_number

def is_master_number(part):
    return part in ['11', '22', '33']

# Example usage:
birthdate = input("Enter your birthdate (MM/DD/YYYY): ")
birthdate_parts = birthdate.split('/')

# Check if any part of the birthdate is a master number
contains_master_number = any(is_master_number(part) for part in birthdate_parts)

if contains_master_number:
    print("Your Life Path Number contains a master number. Calculating...")
    life_path_number = calculate_life_path_number(birthdate_parts)
    print("Your Life Path Number is:", life_path_number)
else:
    print("No master numbers found in the birthdate. Calculating as usual...")
    life_path_number = calculate_life_path_number(birthdate_parts)
    print("Your Life Path Number is:", life_path_number)


