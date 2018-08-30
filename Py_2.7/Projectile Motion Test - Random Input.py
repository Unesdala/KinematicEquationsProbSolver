import math
import random

# Credit to JulianaTh for help with the math equations
#
# Generates a projectile motion problem for the user to solve
# With a random starting height and "x" position.
# Can be used to test knowledge of kinematics.
#
#
# To solve for yourself, remove or comment out print (xend)
#
# Python 2.7


def main():

    # Setup initial numbers
    xinit = round(random.randrange(0,100),0) # X Starting Position
    xvel =  round(random.randrange(0,100),0) # X Velocity
    yinit=  round(random.randrange(0,100),0) # Y Starting Position]
    yvel =  round(random.randrange(0,100),0) # Y Velocity
    t = (-yvel - math.sqrt(yvel*yvel - (2*-9.8*yinit)))/-9.8 # Find Time
    xend = float(projectile(xinit,xvel,t))

    print 'The initial x position is', xinit, 'and velocity is', xvel, '.'
    print 'The initial y position is', yinit, 'and velocity is', yvel, '.'
    print 'Time is ', t, '.'

    print (xend) #For Testing, remove after

    while True:
        studentx = float(input('Enter the final x value: '))

        if (abs((studentx - xend)/xend)) < 0.1: # Within ~10%. Can change to be more or less strict
            print 'That is correct!'
            break
        else:
            print 'That isn\'t correct. Please try again.'


# Function to find X's ending position    
def projectile(xinit,xvel,t):
    xend = xinit + xvel*t
    return xend

main()
