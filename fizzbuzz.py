"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.
"""

def check_if_multiple_of_3(num):
    if num%3 == 0:
        return True
    else:
        return False


def check_if_multiple_of_5(num):
    if num%5 == 0:
        return True
    else:
        return False

def solve_fizzbuzz(num):

        if num == 0:
            raise ValueError
            
        if check_if_multiple_of_5(num) and check_if_multiple_of_3(num):
            return "fizzbuzz"
            
        elif check_if_multiple_of_5(num):
            return "buzz"
            
        elif check_if_multiple_of_3(num):
            return "fizz"
            
        else:
            return num
           

if __name__ == "__main__":
    
    range_num = int(input("Enter the range : (1-100) ? "))

    for num in range(1,range_num+1): print(solve_fizzbuzz(num))