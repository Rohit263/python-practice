import math

def drive():
    # vr = right wheel velocity(rpm)
    # vl = left wheel velocity(rpm)
    # v = translational velocity(m/sec)
    # w = Angular velocity(rad/sec)
    # l = base length or axle length or distance between the left and right wheels(cm)
    # r = radius of the wheel(cm) 
   
   # declraing vr and vl as global variable
    global vr,vl 

    # Calculating the velocities of right and left wheel
    vr = (((2*v) + (w*l))/(2*r)) 
    vl = (((2*v) - (w*l))/(2*r))

   # Printing the wheels velocities after converting them into rpm.
    print(f'''
Output-
Left Wheel Velocity= {((vl*60)/(2*math.pi)):.5f} rpm
Right Wheel Veocity= {((vr*60)/(2*math.pi)):.5f} rpm''')

    


# Start of main function block
if __name__ == '__main__':
    print('Input-')
    r= int(input('Wheel radius(cm): '))
    l= int(input('Wheel base length(cm): '))
    v= int(input('Translational velocity(m/s): '))
    w= int(input('Angular velocity(rad/s): '))
    
    #Calling the drive() function
    drive()

    #Applying the conditions of forward, backward,left and right movement
    if vr>0 and vl>0 and vr==vl:
        print('Movement: Forward')
    elif vr<0 and vl<0 and vr==vl:
        print('Movement: Backward') 
    elif vr>vl:
        print('Movement: Turn Left')
    elif vl>vr:
        print('Movement: Turn Right')