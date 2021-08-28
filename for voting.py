def fun(a):
    if a<18:
        return ('you are not eligible for voting')
    else:
        return ('you are eligible for voting')
a=int(input('enter a number'))
print(fun(a))