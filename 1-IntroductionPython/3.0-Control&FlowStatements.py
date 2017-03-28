#Merhaba Arkadaslar Python Ogrenmeye basladım Ogrendiklerimi burdan sirayla paylasmaya calisagim.
#Kaynak www.dosc.python.org

def ifExample():
    x = int(input('Lütfen integer bir deger giriniz :'))
    if x < 0:
        x = 0
        print ("Negatif değerini değiştirin")
    elif x == 0:
        print ('Zero')
        print ("Negatif değerini değiştirin")
    elif x == 1:
        print ('Sıngle')
    else:
        print("More")

def forExample2():
    global a
    print("\nOrnek 2")
    for a in aylar[:]:
        if len(a) > 6:
            print(a)

def forExample1():
    global aylar, a
    aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağuston", "Eylül", "Ekim", "Kasım",
             "Aralık"]
    for a in aylar:
        print(a, len(a))




#if kullanımı
#ifExample()

# #for ifadesi kualllınımı
#forExample1()
#forExample2()


#for i in range(0,10,3):
#   print(i)

#print(list(range(1,7,2)))

def breakStatement():
    global i
    for i in range(5):
        if i == 3:
            break
        print(i, end=',')


breakStatement() #0,1,2


def continueStatement():
    global i
    for i in range(5):
        if i == 3:
            continue
        print(i,end=',')


continueStatement() #0,1,2,4
