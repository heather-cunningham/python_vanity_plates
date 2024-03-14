# Heather Cunningham 2/5/17
# Python
# Cumulative HW Ch's 2- 6

# Create a MA DMV vanity plate program:
# 
# All characters must be letters or numbers (eg no spaces or punctuation marks)
# Minimum of 2 characters.
# Maximum of 6 characters.
# Must begin with two letters. 
# Cannot have letters and numbers intermixed (eg “MG53TD")
# Numbers must come at the end.
# First number cannot be 0 (zero).

# You are to write a program that will accept a plate request from the user
# and tell the user if the plate does or does not violate the rules above,
# and which rule (just the first one if more than one) the request violates.

def enter_plateID():
    vanity_plate = (input("Enter vanity plate you would like:\n")).upper()
    if(validate_plate(vanity_plate)):
        print("Your new Vanity Plate ID is: " + vanity_plate)
        print("New plates will arrive via mail in 6-8 weeks.")


def find_1st_digit(plateID_Passed):
    first_digi = ''
    for ch in plateID_Passed:
        if ch.isdigit():
            first_digi = ch
            break
    return first_digi


def intermixed_chs(plateID_Passed):
    digit1 = find_1st_digit(plateID_Passed)
        #indexOf of 1st digit in plateID_Passed
    indexOf = plateID_Passed.find(digit1)     
    plate_valid = True
    for i in range((indexOf + 1), len(plateID_Passed)):
        if plateID_Passed[i].isalpha():
            plate_valid = False
            break
        elif plateID_Passed[i].isdigit():
            plate_valid = True  
    return plate_valid                  
        

def validate_plate(plateID):
    if plateID.isalnum():
        #plate_valid = True
        if(len(plateID) >= 2 and len(plateID) <= 6):
            #plate_valid = True
            if plateID.isalpha():
                #plate_valid = True
                return True
            if plateID[0].isalpha() and plateID[1].isalpha():
                if find_1st_digit(plateID) != '0':
                    #plate_valid = True
                    if intermixed_chs(plateID):
                        #plate_valid = True
                        return True
                    else:
                        print("Try again. Plate ID can't have mixed letters and numbers.")
                        print("Numbers can come at the end only.")
                        enter_plateID()
                else:
                    print("Try again. The 1st number can't be zero.")
                    enter_plateID()        
            else:
                print("Try again. Plate ID must begin w/ at least 2 letters.")
                enter_plateID()
        else:
            print("Try again. Plate ID must be 2-6 characters in length.")
            enter_plateID()
    else:
        print("Try again. Plate ID must be alphanumerical characters only.")
        enter_plateID()

        
print("Welcome to the DMV!")
print("Vanity Plate Rules:")
print("-------------------")
print("Your vanity plate must be between 2-6 alphanumerical characters.")
print("It must begin with at least 2 letters.")
print("It can't be a mix of letters and numbers; numbers must come at the end.")
print("And, the first number can't be zero.\n")
enter_plateID()
    
