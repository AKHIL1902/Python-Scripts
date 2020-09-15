#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
#multiples of 3 = 330
#and multiples of 5 = 200
#x = 1
total_sum = 0
for i in range(10):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print total_sum
