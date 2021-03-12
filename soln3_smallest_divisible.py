def div():
    #l_lim = lower limit of the searching range
    #u_lim = upper limit of the searching range


    #declaring x,y,l_lim,u_lim as global variable
    global x,y,l_lim,u_lim
    l_lim =1
    u_lim =1
    values = []

    # Getting the value of lower limit and upper limit of the search for any x and y
    for i in range(x-1):
        l_lim = 10*l_lim 
    u_lim = ((l_lim*10)-1) 

    #Appending all the values that are in search area and is divisible by any given y to a list
    for r in range(l_lim,u_lim+1):
        if r%y==0:
            values.append(r)

    # Finding the smallest value among all the feasible values        
    smallest = min(values)
    print('')
    print(f'Smallest {x} digit number divisible by {y} is: {smallest}')
    

# Start of main function block
if __name__ == '__main__':
    x= int(input("Enter no. of digit: "))
    y= int(input("Enter divisibility number: "))
    
    #Calling of the div() function
    div()
