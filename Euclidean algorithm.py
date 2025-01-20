class Euclidean_Algorithm:
    #initialize the numbers
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    #use the priciple of Euclidean Algorithm
    def GCD(self):
        #cehck if self.b==0
        while self.b!=0:
            #caculate
            self.a , self.b = self.b , self.a % self.b
        return self.a

#check if the number is available
def available_number(num):
    #try if the num can be converted to integer
    try:
        integer = int(num)
        return isinstance(integer,int) and integer >= 0
    #if the number can not be converted, return false
    except ValueError:
        return False
    
#user input the number
num1 = input("Please input the first number")
num2 = input("please input the second number")
if available_number(num1) and available_number(num2):
    num1 = int(num1)
    num2 = int(num2)
    #caculate the gcd
    caculate = Euclidean_Algorithm(num1, num2)
    gcd = caculate.GCD()
    print(f"The greatest common divisor of {num1} and {num2} is {gcd}")
else:
    print("Please enter positive integer")
