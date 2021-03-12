import math

def div():
    #l_lim = lower limit of the searching range
    #u_lim = upper limit of the searching range

    # Getting the value of lower limit and upper limit of the search for any x and y
    l_lim = int(math.pow(10,(x-1)))
    u_lim = ((l_lim*10)-1)

    #Appending all the values that are in search area and is divisible by any given y to a list
    values = [i for i in range(l_lim,u_lim+1) if i%y==0] 
    
    # Finding the smallest value among all the feasible values        
    print(f'''
Smallest {x} digit number divisible by {y} is: {min(values)}''')
    

# Start of main function block
if __name__ == '__main__':
    x= int(input("Enter no. of digit: "))
    y= int(input("Enter divisibility number: "))
    
    #Calling of the div() function
    div()