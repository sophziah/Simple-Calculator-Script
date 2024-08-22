x = int(input("First number: "))
y = int(input("Second number: "))


operations = input("Choose operators: [+, -, *,/, %] ")

if operations == '+':
    print("Result:", x + y)
    
elif operations == '-':
    print("Result:", x - y)
    
elif operations == '*':
    print("Result:", x * y)
    
elif operations == '/':
    print("Result:", x / y)


else:
    print("Error!") 

