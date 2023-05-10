import math

from numpy import mat

class pytagore:
    def __init__(self, ab, ac, bc) -> None:
        self.ab = ab
        self.ac = ac
        self.bc = bc

    def pyt_triangle(self):
        n = None
        ab = self.ab**2
        ac = self.ac**2
        bc = self.bc**2

        if ab + ac == bc:
            print("pytagorean triple")
            print("because ", ab, "+", ac, "=", bc)

        else:
            print("no")
            print("because ", ab, "+", ac, "≠", bc)

    def find_missing_num(self):

        if self.ab == "-" and self.ac != "-" and self.bc != "-":
            # solve
            # a**2 + b**2 = c**2

            # move known number over
            calc = abs(self.ac**2 - self.bc**2)
            
            # a**2 = b-c
            calc = math.sqrt(calc)
            print("missing number: ", calc)
            
        if self.ab != "-" and self.ac == "-" and self.bc == "-":
            n = self.ab/2
            self.triple = [n**2-1, self.ab, n**2+1]
            print(self.triple)
            
        if self.ac != "-" and self.ab == "-" and self.bc == "-":
            n = self.ac/2
            self.triple = [n**2-1, self.ac, n**2+1]
            print(self.triple)

            
        if self.bc != "-" and self.ab == "-" and self.ac == "-":
            n = self.bc/2
            self.triple = [n**2-1, self.bc, n**2+1]
            print(self.triple)
            
        
        if self.ac == "-" and self.ab != "-" and self.bc != "-":
            print("ne?")
            # solve
            # a**2 + b**2 = c**2

            # move known number over
            calc = abs(self.ab**2 - self.bc**2)
            
            # a**2 = b-c
            calc = math.sqrt(calc)
            print("missing number: ", calc)

        if self.bc == "-" and self.ab != "-" and self.ac != "-":
            calc = abs(self.ab**2 + self.ac**2)
            calc = math.sqrt(calc)
            print('missing number: ', calc)

        if self.ab == "-" and self.ac == "-" and self.bc != "-":
            n=[]

            c1 = self.bc**2 - 1
            c1 = math.sqrt(c1)

            print(c1)
            try1 = isinstance(c1, int)
            print(try1)
            if try1:
                print(1)
                n.append(c1)
            
            c2 = self.bc**2 + 1
            c2 = math.sqrt(c2)
            try2 = isinstance(c2, int)
            print(c2)
            if try2:
                print(2)
                n.append(c2)
            
            c3 = 2*self.bc
            try3 = isinstance(c3, int)
            if try3:
                print(3)
                n.append(c3)
            print(c3)
            n1 = n[0]
            print(n)
            triplet = [2*n1, n1**2 + 1, n1**2 - 1]

            print(triplet)
            return triplet



ab = 10
bc = 24
ac = 26

#ab = 675
#bc = 677
#ac = 52


# ab = 575
# ac = 48
# bc = 577
set = pytagore(ab,ac,bc)
aa = set.pyt_triangle()

aa = set.find_missing_num()

# set1 = pytagore(set.triple[0], set.triple[1], set.triple[2])
# set1.pyt_triangle()
# # set.pyt_triangle()
# aa = set.find_missing_num()

# s = pytagore(aa[0], aa[1], aa[2])


# Correct option is A)
# We have pythagorean triplet (2n,n 
# 2
#  −1,n 
# 2
#  +1) where n>1 (natural number)
# Let n 
# 2
#  −1=18
# n 
# 2
#  =19
# n= 
# 19
# ​
#   (not an integer)
# n 
# 2
#  +1=18
# n 
# 2
#  =18−1
# n 
# 2
#  =17
# n= 
# 17
# ​
#   (is not an integer)
# So, let us take 2n=18
# n=9
# ∴ The required triplet is (an integer)
# (18,9 
# 2
#  −1,9 
# 2
#  +1)=(18,81−1,81+1)
# i.e., (18,80,82)
