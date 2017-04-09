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


def f1(a, L=[]):
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))

print()

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

#Keyword Arguemnts
#Fonksiyonumuzu çağırırken anahtar kelime parametre formatı ile çağırıyoruz. keyword=value şeklinde. Örnek olarak aşşağıdaki fonksiyonumuzu inceleyelim.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- this parrot wouldn't ",action)
        print("if you put ", voltage , "volts through it")
        print("-- Lovely plumage the ", type)
        print("-- It's",state)

#bu fonksiyonumuzu çağırırken voltage parametresini zorunlu olarak göndermemiz gerekmektedir. Fakat diğer(state, action, type) parametreler opsiyonel haldedir.Gönderip göndermemek yazılımcıya kalmıştır
#fonksiyonumu çağırırken parametre sıramız voltage,state,action,type şeklindedir.eğer biz parrot() fonksiyonunu çağırırken hangi değerin hangi parametre ile eşleşeceğini belirtmeksek bu sıra ile algılayacaktır.
#fakat biz parametrelerimizi keyword = value şeklinde gönderirsek tanımladığımız sıra ile gönderme zorunluluğumuz olmayacaktır.
parrot(1000)
print()
parrot(1000,"A STIFF")
print()
parrot(state="A STIFF",voltage=1500,action="VOOM")
print()
#Yanlış yapılacabilecek durumlara bakalım şimdide
#Fonksiyonumuz için voltage değeri zorunludur. Fakat biz voltage değeri göndermezsek şeklinde hata verecektir.parrot() missing 1 required positional argument: 'voltage'
#parrot()
#fonksiyonumuzu çağırırken parrot() ilk değeri keyword=value şeklinde gönderip ikinci değerimizi sadece value şeklinde göndermek bize syntax hata verecektir.
#İlk parametremizi value sonraki parametrelerimizi key=value şeklinde gönderebiliyoruz.
#parrot(voltage=1000,"dead")
parrot(1000,state="A STIFF",action="VOOM")
# bir sonraki örneğimizde fonksiyonumuzun birinci beklemiş olduğu parametre voltage değeri biz bunu doğru gönderiyoruz fakat voltage değerini daha sonra key=value şeklinde göndermeye çalışıyoruz.
# Aynı argüman için çok değer göndermiş oluyoruz.Bu işlemde bize hata ile dönecektir.
#parrot(100,voltage=555)


print()
print()
#Sıradaki örneğimizde Javada kullanılan varargs yapısına benzer bi yapıyı inceleyeceğiz.
#Burada *arguments ve **keywords şeklinde iki farklı yapı vardır.
# *arguments yapısı Javada kullanılan Varargs yapısına benzemektedir.arguments değişkeni bize dizi şeklinde gelmekteydi bizde onu sıfır, bir veya daha fazla elemanlı dizi olarak işlemekteydik.
#**keywords yapısıda buna benzemektedir. Fakat bundan ayrıcalığı key değerleri de vardır. Javadaki Enumlara benziyor gibiler Enumlar sabit boyutlu idi tanımlandıktan sonra.

def cheeseshop(kind, *arguments,**keywords):
    print( "-- Do you Have any kind ", kind,"?")
    print( "-- I'm Sorry we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        if kw=="client":
            print(kw, ":", keywords[kw].upper())
        else:
            print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

