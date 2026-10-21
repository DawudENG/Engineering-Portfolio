#Import libraries 
import matplotlib.pyplot as plt
import numpy as np

#Define constants
GRAVITY_ACCELERATION = 9.81 #m/s^2
MASS = 280 #Kg
COG_HEIGHT = 0.25 #centre of gravity height #metres
WHEELBASE = 1.59 #metres  
FRONT_WEIGHT_DISTRIBUTION = 0.5

#predefine lists
front_brake_list =[]
rear_brake_list = []
const_frict_list = []

#define constant x function for Friction coefficient lines (these will read the braking values)
x = np.linspace(0,3000,200)


#Loop using each value of u to calculate data points using braking curve theory
for num in np.arange(0, 1.1, 0.1):

    #define and reset front and rear loads
    FRONT_LOAD = MASS * GRAVITY_ACCELERATION * FRONT_WEIGHT_DISTRIBUTION
    REAR_LOAD = (MASS * GRAVITY_ACCELERATION) * (1 - FRONT_WEIGHT_DISTRIBUTION)
        
    #friction coefficient 0<u<1                  
    FRICTION_COEFFICIENT = num

    #Deceleration calculation  a = ug                               #calculate deceleration 
    DECELERATION = FRICTION_COEFFICIENT * GRAVITY_ACCELERATION

    #Transferred load from rear to front calculation                #use this value to calculate load transfer
    LOAD_TRANSFER = (MASS * DECELERATION * COG_HEIGHT) / WHEELBASE  #F(transfer) = ma D(COG) / D(wheelbase)

    #Update front and rear normal loads by transferred
    FRONT_LOAD += LOAD_TRANSFER                                 #add load transfer to front load as it gains from rear
    REAR_LOAD -= LOAD_TRANSFER                                  #subtract load from rear as it givse load to front

    #Calculate Front and Rear braking forces
    front_brake_force = FRICTION_COEFFICIENT * FRONT_LOAD        #use F = uR, To calculate brake forces, where R is the Normal force of each axle (front and rear loads)
    rear_brake_force = FRICTION_COEFFICIENT * REAR_LOAD          #using values of the loads for each axle

    #Add brake forces to list
    front_brake_list.append(float(front_brake_force))
    rear_brake_list.append(float(rear_brake_force))

    #Create line function y = umg - x
    y = (FRICTION_COEFFICIENT * MASS * GRAVITY_ACCELERATION) - x    #y = umg - x   is used to create diagnol line at each friction coefficient point
    #append to line list                                              
    const_frict_list.append(y)



#Plotting code


#create and adjust axes
fig, ax = plt.subplots(figsize=(25,10))      #sets display axis 25 inches horizontally, 10 inches vertically
#make grid
ax.grid(alpha=0.5)      #sets a grid structure where alpha halves opacity to make grid feint

#plot data

#brake curve
ax.plot(front_brake_list, rear_brake_list, linewidth = 1.0, color = 'black')   #plots curve on axis, linewidth 1px, black color

#y = umg - x
for count in np.arange(0,11):                                               #This code iterates through each friction coefficient value and 
    ax.plot(x, const_frict_list[count], color = 'black', linewidth = 0.5)   #it plots the lines y = umg - x  for each value

#label each point with coefficient number
for label in np.arange(0.1, 1.1, 0.1):
    ax.text( (2750 * label) ,10, f'{round(label,1)}')       #mathematically approximate label points and place values to show them



#adjust graph and name axes
ax.set(xlim=(0,3000), xticks = np.arange(0,3000,250),   #xlim sets limit of x axis 0 - 3000, ticks display intervals every 250 units
       ylim=(0,1000), yticks = np.arange(0,1000,100),   #ylim sets limit of y axis 0 - 1000, ticks display intervals every 100 units
       xlabel='Front Brake Force (N)', #x label
       ylabel='Rear Brake Force (N)', #y label
       title='Ideal Brake Curve'            ) #title
         

#show plots
plt.show()



