def check_number(n):
    if n % 2 != 0:
        print("Wierd")
    elif 2 <= n <= 5:
        print("Wierd")
    elif 6 <= n <= 20:
        print("Wierd")
    elif n > 20:
        print("Not Wierd")
        
        
n = int(input("Enter an integer:"))
check_number(n)