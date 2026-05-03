class fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def __mul__(self,other):
        if isinstance(other, fraction):
            new_fraction = fraction(self.num*other.num,self.den*other.den)
        else:
            new_fraction = fraction(self.num*other,self.den)
        return new_fraction
    def GCD(self,other):
        if (other.den % self.den == 0):
            return other.den
        elif (self.den % other.den == 0):
            return self.den
        else:
            c = 2
            while True:
                if (self.den % c == 0) and (other.den % c == 0):
                    return c 
                else:
                    c+=1
    def self_GCD(self):
        if (self.num % self.den == 0):
            return self.den
        elif (self.den % self.num == 0):
            return self.num
        else:
            c = 2
            while True:
                if (self.den % c == 0) and (self.num % c == 0):
                    return c 
                else:
                    c+=1
                if c == 10000:
                    return "no common divisor"
    def __add__(self,other):
        if isinstance(other, fraction):
            gcd = self.GCD(other)
            temp_den1 = gcd // self.den
            temp_den2 = gcd // other.den
            temp_num1 = self.num * temp_den1
            temp_num2 = other.num * temp_den2
            temp_add = temp_num1 + temp_num2
            return fraction(temp_add,gcd)
        else:
            temp_frac = fraction(other,1)
            return(self+temp_frac)
    def __str__(self):
        if self.num == 0:
            return f"{self.num}"
        elif self.num == self.den:
            return f"1"
        else:
            return f" {self.num}\n---\n {self.den}"
    def simplifcation(self):
        temp_gcd = self.self_GCD()
        if temp_gcd == "no common divisor":
            print(f"\n\ncannot simplify the fraction, no common divisor was found!")
            return self
        else:
            temp_num = self.num // temp_gcd
            temp_den = self.den // temp_gcd
            return f"{fraction(temp_num,temp_den)}"
print("\n\n")
a = fraction(1,2)
b = fraction(1,4)
c = fraction(2,4)
new = a+b
new1 = a*b
new2 = a*3
new3 = a+4
print("\nfraction addition\n",new,"\n==========",sep="")
print("\nfraction multiplcation\n",new1,"\n==========",sep="")
print("\nfraction and number multiplcation\n",new2,"\n==========",sep="")
print("\nfraction and number addition\n",new3,"\n==========",sep="")
print("\nsimplifcation\n",c.simplifcation(),"\n==========",sep="")

print("\n\n")

