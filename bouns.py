

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)

def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)

def main():
 while True:  
   massege = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
   try:
    ele= massege.split()   

    num=float(ele[0])
    unit=ele[1].upper()
       
    if unit =="F":
      res= fahrenheit_to_celsius(num)
      print("Temperature in Celsius:",res,"C")
      break
    elif  unit =="C":
        res= celsius_to_fahrenheit(num)
        print("Temperature in Fahrenheit",res,"F")
        break
    else:
     raise TypeError("invaild unit")     
   except ValueError :
    print("invalid  temperature ,try agine")
   except TypeError :
        print("try agine")
   except IndexError  :
     print("pls enter tem and uint")   
   except Exception as e:
        print(e)   

main()         

   




    
