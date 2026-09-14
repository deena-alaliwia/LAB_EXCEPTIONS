def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10,20)
except  NameError:
    print(" invalid var ")
except  TypeError :  
    print(" worng we have miss match error")  
except Exception as e:
    print(" somting is wrong ",e) 


