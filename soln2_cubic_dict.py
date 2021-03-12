def cubic_dict():
    # Declaring cubic_book as global variable
    global cubic_book

    #Generating a list containing numbers from 1 to 10 
    numbers = [i for i in range(1,11)]

    #Generating a list containing cubes of the numbers from list 'numbers'
    cubes = [(j*j*j) for j in range(1,11) ]

    #Creating a dictionary with keys = elements of list 'numbers' and values = elements of list cubes
    cubic_book = dict(zip(numbers,cubes))   
    return cubic_book


#Start of the main function block
if __name__ == '__main__':

    #Calling the cubic_dict() function
    print(cubic_dict())

    #Printing the only element among the values of the dictionary that is divisible by both 5 and 2
    for i,j in zip(cubic_book.keys(),cubic_book.values()) :
        if j%5==0 and j%2==0:
            print(f'Key of value divisible by 2 & 5 is: {i}')   
    
    
