while True:
    c=str(input("Which order derivative you want to do?(1/2): "))
    if c=="1":
        import numpy as np

        def f(x):
            return eval(function)

        function=str(input("enter function to derivative: "))
        x0=float(input("enter at which point you want the result: "))
        h=0.001

        a=(1/(2*h))*(f(x0+h)-f(x0-h))

        print("result: ",round(a))
        d1=str(input("do you want to continue?(y/n): "))
        if d1=="n":
           break
        
    elif c=="2":
       import numpy as np
       
       def f(x):
           return eval(function)
      
       function=str(input("enter function to derivative: "))
       h=0.001
       x0=float(input("enter at which point you want the result: "))
      
       b=(1/(h**2))*(f(x0+h)-2*f(x0)+f(x0-h))
       print("result: ",round(b))
    
       d2=str(input("do you want to continue?(y/n): "))
       if d2=="n":
          break
print("Thank you")