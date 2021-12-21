print("How to use equadiff(a,b,c,x0,y0) ?\nThe variables are here:\ncy'+ay = b\ny(x0)=y0\n\nBy default b=0 and c=1\nx0 and y0 are undefined")
def equadiff(a,b=0,c=1,x0=0,y0=0):
    a=simplify(-a,c)
    if(b!=0): b = simplify(b, c)
    if(x0==0 and y0==0):
        print("for all k in R")
        if(b == 0):
            return 'y=ke^'+a+'x'
        else:
            return 'y=ke^('+a+'x)'+simplify(num(b)*den(a),den(b)*num(a),True)
    else:
        if(b==0):
            if(x0<0):
                return 'y='+str(y0)+'e^'+a+'(x+'+str(abs(x0))+')'
            else:
                return 'y=' + str(y0) + 'e^' + a + '(x-' + str(abs(x0)) + ')'
        else:
            k = simplify(y0*den(b)*num(a)-num(b)*den(a),den(b)*num(a))

            if(x0<0):
                return 'y='+k+'e^('+ str(a) + '(x+' + str(abs(x0)) + '))'+simplify(num(b)*den(a),den(b)*num(a),True)
            else:
                return 'y='+k+'e^(' + str(a) + '(x-' + str(abs(x0)) + '))'+simplify(num(b)*den(a),den(b)*num(a),True)


def gcd(a,b):
    a=int(abs(a))
    b=int(abs(b))
    common = 1
    for n in range(1,b+1):
        if(a%n == 0 and b%n == 0):
            common = n
    return common

def simplify(a,b,sign=False):
    a= int(a)
    b= int(b)
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

def num(fraction):
    fraction = str(fraction)
    num = fraction.split("/")[0]
    if(len(num.split("(")) == 2):
        num = num.split("(")[1]
    return int(num)

def den(fraction):
    fraction = str(fraction)
    if(len(fraction.split("/"))==2):
        den = fraction.split("/")[1]
        den = den.split(")")[0]
    else:
        den = 1
    return int(den)
