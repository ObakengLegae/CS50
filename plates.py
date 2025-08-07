'''
“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end. For example, 
    AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
        The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”
'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if digit_alpha(s) is True:
        return True
    else:
        return False

def digit_alpha(plate):

    if confirm(plate) is True:
            
        if plate.isalpha():
            return True
        
        else:

            for i in list(plate):

                if i.isdigit() and i == '0':
                    return False
            
                elif i.isdigit():
                    current_char = plate.index(i)         
                    new_list = plate[current_char:]

                    result = all(item.isdigit() for item in new_list)
                    
                    return result
    else:
        return False

def confirm(plate):
    if character_limit(plate) is True and first_letters(plate) is True and is_alnum(plate) is True:
        return True
    else:
        return False
#   Character limit
def character_limit(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False

#  First two letters
def first_letters(plate):
    first_letters = plate[:2]
    if first_letters.isalpha():
        return True
    else:
        return False

#  Is Alnum
def is_alnum(plate):
    if plate.isalnum():
        return True
    else:
        return False
    
main()
