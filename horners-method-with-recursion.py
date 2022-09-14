# Recursive polynomial evaluation using Horner's method and recursion

def eval(coef, xval):
    if not coef: return 0
    return coef[0] + (xval*eval(coef[1:], xval))


print(8*4**5 + 2*4**4 + 7*4 + 1) # f(4) = 8x^5 + 2x^4 + 7x + 1
print(eval([1, 7, 0, 0, 2, 8], 4)) # f(4) = 8x^5 + 2x^4 + 7x + 1