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
    
#caculate the gcd
caculate = Euclidean_Algorithm(270,192)
gcd = caculate.GCD()
print(f"The greatest common divisor 270 of 192 and is {gcd}")

