import math
import random

# Credit to JulianaTh for help with the math equations
#
# Generates a projectile motion problem for the user to solve
# With a random starting height and "x" position.
# Can be used to test knowledge of kinematics.
#
# To solve for yourself, remove or comment out print (xend)
#
# Python 3.6.1

def main():

    # Setup initial numbers
    xinit = round(random.randrange(0,100),0) # X Starting Position
    xvel =  round(random.randrange(0,100),0) # X Velocity
    yinit=  round(random.randrange(0,100),0) # Y Starting Position]
    yvel =  round(random.randrange(0,100),0) # Y Velocity
    t = (-yvel - math.sqrt(yvel*yvel - (2*-9.8*yinit)))/-9.8 # Find Time
    xend = projectile(xinit,xvel,t)
    yend = 0

    print("The initial x position is", xinit, "and velocity is", xvel, ".")
    print("The initial y position is", yinit, "and velocity is", yvel, ".")
    print ("Time is ", t)

    print ("X End:",xend) #Testing Purposes, remove for final

    while True:
        studentx = input("Enter the final x value: ")
        studentx = float(studentx)

        if xend == studentx:
            print("That is correct!")
            break
        else:
            print("That isn't correct. Please try again.")

    
def projectile(xinit,xvel,t):
    xend = xinit + xvel*t
    return xend

main()
