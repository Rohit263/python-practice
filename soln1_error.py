def error():
    try: 
        out = 1/0
        print(out)
        print('Division by Zero accomplished.')
    except:
        print('Error:root:Division by Zero Error')
        

if __name__ == '__main__':
    error()
    print('Entered in final block')