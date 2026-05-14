def fact(val):
    if val ==1 or val ==0:
        return 1
    return val*fact(val-1)

print("give the number to factorial")
val = int(input())
print(fact(val))