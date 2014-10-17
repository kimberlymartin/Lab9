############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

patient = True

while patient == True:
    print "New patient."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "What is your temperature?"
    temp = int(raw_input())
    print "Have you been sick in the past 24 hours?"
    sick = raw_input()
    print "Have you recently travelled to West Africa?"
    africa = raw_input()
    if temp > 105:
        print "You need to be admitted to the hospital."
    elif temp > 102 and sick == 'yes':
        print "You need to be admitted to the hospital."
    elif temp > 100 and africa == 'yes':
        print "You need to be admitted to the hospital."
    elif sick == 'yes' and africa == 'yes':
        print "You need to be admitted to the hospital."
    else:
        print "You do not need to be admitted to the hospital."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Is there another patient?"
    another = raw_input()
    if another == 'no':
        patient = False