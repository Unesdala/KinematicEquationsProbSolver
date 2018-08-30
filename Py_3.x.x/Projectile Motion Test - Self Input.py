import math
import random

# Credit to JulianaTh for help with the math equations
#
# Solves projectile motion problems using
# user input X starting position and velocity
# And user input Y starting position and velocity.
#
# Python 3.6.1

def main():

    # Setup initial numbers
    xinit = float(input("Enter the starting X value: ")) # X Starting Position
    xvel =  float(input("Enter the starting X velocity: ")) # X Velocity
    yinit=  float(input("Enter the starting Y value: ")) # Y Starting Position]
    yvel =  float(input("Enter the starting Y velocity: ")) # Y Velocity
    t = (-yvel - math.sqrt(yvel*yvel-(2*-9.8*yinit)))/-9.8 # Find Time
    xend = projectile(xinit,xvel,t)

    print("The initial x position is", xinit, "and velocity is", xvel, ".")
    print("The initial y position is", yinit, "and velocity is", yvel, ".")
    print ("Time is ", t)

    print ("X End: ",xend)
    
def projectile(xinit,xvel,t):
    xend = xinit + xvel*t
    return xend

main()
