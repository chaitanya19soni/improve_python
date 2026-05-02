def fibo (num):
    sum = 0
    n1,n2 = 0 ,1
    while(num >sum):
        n1 = n2 
        n2 = sum 
        sum = n1+n2
num =  int (input ())
fibo(num)