def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return(res)

if __name__ == '__main__':
    print(factorial(2))
