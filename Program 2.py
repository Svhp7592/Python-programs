def multiplication_table(number):
    for i in range(1, 12):
        print(f"{i}*{number}= {i*number}")
        
number=int(input("Enter a number: "))
multiplication_table(number)