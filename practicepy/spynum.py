def spynum(n):
    digits = [int(d) for d in str(n)]
    digit_sum = sum(digits)
    digit_product =1
    for d in digits:
        digit_product *= d
    return digit_sum == digit_product
    
num =  int(input("enter the number"))    

if spynum(num):
    print(f"{num} is a spynumber")
else:
    print(f"{num} is not a spynumber")











