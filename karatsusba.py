def multiply(x,y):
    if(len(x) < len(y)):
        x ='0'*(len(y)-len(x))+x
    elif(len(y) < len(x)):
        y ='0'*(len(x)-len(y))+y
    if(len(x) == 1):
        return int(x)*int(y)
    a = x[0:len(x)//2]
    b = x[len(x)//2:len(x)]
    c = y[0:len(y)//2]
    d = y[len(y)//2:len(y)]

    ac = multiply(a,c)
    bd = multiply(b,d)
    a_plus_b = str(int(a)+int(b))
    c_plus_d = str(int(c)+int(d))
    ad_plus_bc = int(multiply(a_plus_b,c_plus_d))-ac-bd

    # ac*10^n + bd + (ad + bc)*10^(n/2)
    # ad + bc = (a + b)(c + d) - ac -bd
    result = int(str(ac)+'0'*len(x))+bd+int(str(ad_plus_bc)+'0'*(len(x)//2))
    return result

if __name__=="__main__":
    print(multiply("00150000","00120000"))
    #print(multiply("3141592653589793238462643383279502884197169399375105820974944592","2718281828459045235360287471352662497757247093699959574966967627"))
