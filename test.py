def fun(num):
    if num>=0:
        print(num)
        return fun(num-1)    
fun(5)    