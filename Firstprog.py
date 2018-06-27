hrs = input("Enter Hours:") 
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)


if h <= 40:
    grs_pay = h * r
    print (grs_pay)
    
if h > 40:
    grs_pay = (40 * r) + (1.5 * r *(h - 40))
    print (grs_pay)

print (type (grs_pay))
#raw_input was used in python 2 but just input() is used in Python 3
#For printing output "print x" was used, but now () should be included
