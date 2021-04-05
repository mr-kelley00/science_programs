# Velocity, Acceleration, and Force Calculator, Ryan Kelley, 04/05/21, 10:10AM, Version 0.0 

import time 

calc_again = "Yes"

def vaf_calculator(): 
    global distance, time_initial, time_final, velocity_initial, velocity_final, mass, acceleration, force, calc_again

    print("This program will help you calculate the velocity, acceleration, and force of an object moving in a straight line.\n")
    print("This program assumes that all objects are starting from a standstill.\n")
    print("First, you will need to collect some measurement data on the object.\n")
    time.sleep(3)

    mass = float(input("Please enter the mass of the object in grams.  Type just the number and press enter.\n"))

    print(f"The mass of your object is {mass} grams.\n")
    time.sleep(3)

    print("The first value I will need to calcualte is the velocity of the object.  You will need the data from your data sheet collected in class.\n")

    distance = int(input("Please enter the distance measured in meters.  Type only the numbers and press enter.\n"))
    time_final = float(input("Please enter the time it took for the object to travel that distance.  Type only the numbers and press enter.\n"))

    print(f"Your object traveled {distance} meters in {time_final} seconds.\n")

    x = 0
    while x < 5:
        print("Calculating...\n")
        x += 1
        time.sleep(1)
    
    velocity_final = (distance / time_final)
    print(f"The calculated velocity is {velocity_final} m/s [meters per second].\n")

    print("Now that the velocity has been calculated, this program can now calculate the rate of acceleration and the amount of force on the object.\n")

    x = 0
    while x < 5:
        print("Calculating...\n")
        x += 1
        time.sleep(1)

    velocity_initial = 0.0
    time_initial = 0.0 
    acceleration = (velocity_final - velocity_initial) / (time_final - time_initial)
    
    print(f"The acceleration of the object was {acceleration} m / s^2 [meters per second squared].")

    x = 0
    while x < 5:
        print("Calculating...\n")
        x += 1
        time.sleep(1)

    force = mass * acceleration
    print(f"The force on the object was {force} N [Newtons].")

    calc_again = input("Do you want to run another calculation? Type yes or no, then press enter.\n")

    if calc_again == "Yes" or calc_again == "yes" or calc_again == "y":
        print("Ok, let's restart the calculations.\n")
    else: 
        print("Ok, thank you.  I hope this program was useful.\n")
    

while calc_again == "Yes" or calc_again == "yes" or calc_again == "y":
    vaf_calculator() 







