a=10
b=5
try:    
    d=a/b
    print(d)
    print("inside try")

except ZeroDivisionError:
        print("divison by zero not allowed")
else:
    print("inside else")
print("rest of the code")

        