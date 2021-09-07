
#lower
l = 1

#upper
u = 115792089237316195423570985008687907853269984665640564039457584007913129639936

print("Prime numbers between", l, "and", u, "are:")

for num in range(l, u + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
