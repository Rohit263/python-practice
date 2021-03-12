import math

def constraints():

    global xi,yi,xf,yf

    #Final value
    xf = ((xi+right)-left)
    yf = ((yi+up)-down)

    #Printing final coordinates
    print(f"Final Position: {xf},{yf}")  
    print('')  

    #Calculating euclidian distance
    euclid = math.ceil(math.sqrt((math.pow((xf-xi),2))+ (math.pow((yf-yi),2))))
    print(f'Distance: {euclid}')
    print('')

    #Conditions for getting quadrants
    if xf>0 and yf>0:
        print('First Quadrant')

    elif xf<0 and yf>0:
        print('Second Quadrant')

    elif xf<0 and xf<0:
        print('Third Quadrant')

    elif xf>0 and yf<0:
        print('Fourth Quadrant')

    else:
        print('Origin')


if __name__=="__main__":
    #initial value
    xi =0
    yi =0
    
    while True:
        up = int(input("UP "))
        down = int(input("DOWN "))
        left = int(input("LEFT "))
        right = int(input("RIGHT "))
        print('')
        constraints()
        query = str(input('Continue with same position(y/n) or end the program(s): ').lower())

        if query == 'yes' or query == 'y':
            print(xf,yf)
            xi=xf
            yi=yf
        elif query == 'no' or query == 'n':
            xi = 0
            yi = 0
        elif query == 's':
            print('')
            print('Shutting Down Program')
            break
        else:
            print('Invalid Entry!')
            print('Try again')
            print('')
            pass