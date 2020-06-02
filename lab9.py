"""
lab9
"""
#3.1
class my_stat():
    def calcsig(self,m,n):
        self.result = 0
        for i in range (m,n+1):
            self.result = self.result + i
            
        return self.result
        
    def calcpi(self,m,n):
        self.result = 1
        for i in range(m,n+1): 
            self.result = self.result * i

        return self.result
        
    def calcf(self,m):
        if m == 0:
            return 1
        else:
            return m * self.calcf(m-1)
            
    def calcp(self,m,n):
        return self.calcf(m)/self.calcf(m-n)


#3.2
my_cal = my_stat()
print(my_cal.calcsig(3,5))
print(my_cal.calcpi(3,5))
print(my_cal.calcf(5))
print(my_cal.calcp(5,3))