from sys import argv

script, number_1, number_2 = argv
import math

print " Welcome to my calculator"
option_1 = ('+')
option_2 = ('-')
option_3 = ('*')
option_4 = ('/')
number_1 = int(raw_input("Please enter your number: \n"))
number_2 = int(raw_input("Please enter your number: \n"))
print number_1
print number_2
print "Please choose the option you want  \n%r,\n%r,\n%r,\n%r" %(option_1,option_2,option_3,option_4) #problem 2 i am trying to print variables by making it strings not good

response = raw_input()

def cal_c():

    if response == option_1:#problem one was notice the spacing between if response and elif response i gave them symmetry and aligned with elif response 
	   return(number_1 + number_2)# nope its not error one lets see the spaces before return
    elif response == option_2:
	   return(number_1 - number_2)#syntax erro it is elif not elseif
    elif response == option_3:
	   return(number_1 * number_2)# eror 4 unindent doesnt match outer level..i guess its about the spaces before return
    elif response == option_4:
	   return(number_1 / number_2)#error 1 unexpexted indent ..i guess its space after : ill will fix it lets see
    else:
	
	
	   print " I do not understand that"# nope i guess its about the space between return   ()
print cal_c()#also i forgot to print the cal_c
#error for unexpected indent was i wasnt declaring the funtion and it linked wit response
#I have cleared the spaces between lines and every where and i have also cleared thecomment after the logic true statement
#still not working same unindent does not match outer indent level error
# now problem 2 is compiler is giving asking for raw input before displaying the option
#coz i declared response variable before printing the options so i will fix it by replacing response with printing options..