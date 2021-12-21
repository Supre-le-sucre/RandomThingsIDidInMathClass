print("How to use equadiff(a,b,x0,y0) ?\nThe variables are here:\ny'+ay = b\ny(x0)=y0\n\nBy default b=0\nx0 and y0 are undefined")
def equadiff(a,b=0,x0=0,y0=0):
    a=-a
    if(x0==0 and y0==0):
        print("for all k in R")
        if(b == 0):
            return 'y=ke^'+str(a)+'x'
        else:
            return 'y=ke^('+str(a)+'x)'+simplify(-b,a,True)
    else:
        if(b==0):
            if(x0<0):
                return 'y='+str(y0)+'e^'+str(a)+'(x+'+str(abs(x0))+')'
            else:
                return 'y=' + str(y0) + 'e^' + str(a) + '(x-' + str(abs(x0)) + ')'
        else:
            k = simplify(y0*a+b,a)
            if(x0<0):
                return 'y='+k+'e^('+ str(a) + '(x+' + str(abs(x0)) + '))'+simplify(-b,a,True)
            else:
                return 'y='+k+'e^(' + str(a) + '(x-' + str(abs(x0)) + '))'+simplify(-b,a,True)


def gcd(a,b):
    a=int(abs(a))
    b=int(abs(b))
    common = 1
    for n in range(1,b+1):
        if(a%n == 0 and b%n == 0):
            common = n
    return common

def simplify(a,b,sign=False):
    if(sign):
        sign="+"
        if(a<0 and b<0): sign="+"
        elif(a<0 or b<0): sign="-"
        else: sign="+"
    else:
        sign = ""
        if (a < 0 and b < 0):
            sign = ""
        elif (a < 0 or b < 0):
            sign = "-"
        else:
            sign = ""
    while(gcd(a,b) != 1):
        divise=gcd(a,b)
        a=int(a/divise)
        b=int(b/divise)
    if(b == 1 or b==-1): return sign+str(abs(a))
    else: return sign+'('+str(abs(a))+'/'+str(abs(b))+')'


print(equadiff(10,-67))
