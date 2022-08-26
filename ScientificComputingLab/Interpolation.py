#Linear Interpolation 
import sympy as sp

def linear_interpolate(x, x1, y1, x0, y0):
    a, b = sp.symbols("a b")
    y = y0+((y1-y0)/(x1-x0))*(x-x0)
    expr = (y0+((y1-y0)/(x1-x0))*(a-x0))
    print("f(b) : ", expr)
    return y

def quadratic_interpolate(x, x1,y1, x2, y2, x3, y3):
    a, b = sp.symbols("a b")
    b0 = x1
    b1 = (y2-y1)/(x2-x1)
    b2 = ((y3-y2)/(x3-x2))-((y2-y1)/(x2-x1))
    b2/=(x2-x1)
    y = b0+b1*(x-x1)+b2*(x-x1)*(x-x2)
    expr = b0+b1*(a-x1)+b2*(a-x1)*(a-x2)
    print("f(x) = ", expr)
    return y

def finite_divident(arr, pairs):
    if len(arr)==2:
        return (pairs[arr[1]]-pairs[arr[0]])/(arr[1]-arr[0])
    elif len(arr)==1:
        return pairs[arr[0]]
    
    else:
        a = finite_divident(arr[0:len(arr)-1], pairs)
        #print(arr[0:len(arr)-1], a)
        b = finite_divident(arr[1:], pairs)
       #print(arr[1:], b)
        x = (b-a)/(arr[-1]-arr[0])
        return x
    

def newton_divident(x, pairs, ls, n):
    a = sp.symbols("a")
    polys = []
    for i in range(0, n):
        polys.append(sp.symbols("x"+str(i)))
    expr = pairs[ls[0]]
    for i in range(1, n):
        arr = []
        mul = 1
        for j in range(0, i):
            arr.append(ls[j])
            mul=  mul*(a-ls[j])
        expr = expr+mul*(finite_divident(arr, pairs))
    print(expr)


#1
print("f(0) : ", linear_interpolate(0, 2, 1, -1, -8))
print("f(5) : ", linear_interpolate(5, 9, 15, 5, 12))

#2
print("f(2.5) : ", quadratic_interpolate(2.75, 0, 659, 2, 705, 3, 729))


#3
quadratic_interpolate(0, 0, 0, 1, 1, 2, 20)

#4
pairs = {1.0: 0.7651977, 1.3:0.6200860, 1.6: 0.4554022, 1.9: 0.2818186, 2.2: 0.1103623}
ls = [1.0, 1.3, 1.6, 1.9, 2.2]
n = 5
newton_divident(0, pairs, ls, n)