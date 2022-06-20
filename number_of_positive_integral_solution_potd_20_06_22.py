from cmath import e
from math import factorial as fact


def posIntSol(s):
    test = s.split('=')
    num = int(test[1].strip())
    #print(num)
        
    #test = s.split('=')
    a = (s.count('+')+1)
    #a = a+1
        
    if num < a:
        return 0
    else:
        return (fact(num-1)// (fact(a-1)*fact(num-a)))
    
 
    # num = 0
    # for m in s:
    #     if m.isdigit():
    #         num =  m
    # num = int(num)
    # print(num)
    # a = (s.count('+')+1)
    # return ( ((num-1)*(num-2)) // a )
    # test = s.split('=')
    # var = len(test[0].strip().split('+'))
    # total = int(test[1].strip())
    # if var > total:
    #     return 0
    # else:
    #     return (fact(total-1)//(fact(var-1)*fact(total-var)))


print(posIntSol("a+b+c+d+f=475"))