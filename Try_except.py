largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
          break
    
    try:
       x = int(num)
              
    except ValueError:
       print ("Invalid input")
       continue
    if largest is None and smallest is None:
        largest = x
        smallest = x
    if x > largest:
           largest = x
    elif x < smallest:
           smallest = x
       
print ("Maximum is"), largest
print ("Minimum is"), smallest
