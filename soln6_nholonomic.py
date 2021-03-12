import math

def constraints():

    global xi,yi,xf,yf

    #initial value
    xi =0
    yi =0

    #Final value
    xf = ((xi+right)-left)
    yf = ((yi+up)-down)

    #Printing final coordinates
    print(f"Final Position (x, y): {xf}, {yf}")   

    #Calculating euclidian distance
    euclid = float(math.ceil(math.sqrt((math.pow((xf-xi),2))+ (math.pow((yf-yi),2)))))
    print(f'Distance: {euclid}')

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
    up = int(input("UP "))
    down = int(input("DOWN "))
    left = int(input("LEFT "))
    right = int(input("RIGHT "))
    print('')
    constraints()
    