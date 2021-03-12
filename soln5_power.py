def pow():
    poo=1

    #Multiplying any x , y number of times to get the value of pow(x,y)
    for i in range(y):
        poo = x*poo
    print(f'{x}^{y}= {poo}')


#Start of the main function block
if __name__ == '__main__':
    x= int(input('Base: '))
    y= int(input('Power: '))

    #Calling the  pow() function
    pow()