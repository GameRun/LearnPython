#Merhaba Arkadaslar Python Ogrenmeye basladım Ogrendiklerimi burdan sirayla paylasmaya calisagim.
#Kaynak www.dosc.python.org

def fib(n):
    """Print Fibonacci Series"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fibonacci(n):
    """Print Fibonacci Series"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


fib(42)

a = fibonacci

print(a(500)[1:5], a(500)[-5:len(a(500))])
print(a(500)[1:6])


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask=ask_ok('Do you really want to quit?',2, 'Come on, only yes or no!')

# if ask :
#    print("Hos geldin Kamill")
# else:
#    print("Yuh dede")

i = 5

def f(arg=i):
    print(arg)


fdef = f

f(6)
fdef()
