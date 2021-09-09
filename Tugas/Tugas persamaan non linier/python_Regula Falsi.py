# Defining Function
def f(x):
    return x**2-27


# Implementing False Position Method
def falsePosition(x0,x1,e):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


# Input Section
x0 = input('a: ')
x1 = input('b: ')
e = input('Toleransi galat: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Tidak ada akar, asumsikan ulang nilai batas a dan b.')
    print('Coba lagi dengan angka yang berbeda')
else:
    falsePosition(x0,x1,e)
