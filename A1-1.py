#function to calculate the sum of digit using recursion
#find the last digit with modulo (reminder) and keep dividing with floor until single digit
def sum_of_digits(n):
    if n<10:
        return n
    return n % 10 + sum_of_digits(n//10)

#input from the user until single digit number is entered with while loop
#call the function and display the result
n=int(input("Input: "))
result=sum_of_digits(n)
print("Output:", result)
while n>=10:
    n=int(input("Input: "))
    result=sum_of_digits(n)
    print("Output:", result)

    

##other option for recursion
# def user_input():
#     n=int(input("Input: "))
#     result=sum_of_digits(n)
#     if n<10:
#         print("Output:", result)
#     else:
#         print("Output:", result)
#         user_input()

# user_input()
