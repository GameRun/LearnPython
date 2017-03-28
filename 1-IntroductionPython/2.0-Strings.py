#Merhaba Arkadaslar Python Ogrenmeye basladım Ogrendiklerimi burdan sirayla paylasmaya calisagim.
#Kaynak www.dosc.python.org

#Temel String'ler ile yaptigimiz islemleri inceleyecegiz.
#String ifadeleri tek veya çift içerisine yazıyoruz.
#print() fonksiyonu içerisinde degisenkeri , (virgül) ile ayırabiliriz.
print("spam" , 'karga')

print( "Selam's")

print(' "yes," he said' )
#Kod içerisinde tırnak ifadesi kullnacaksak javada ters slash ifadesi kullanmamız gerekmektedir.
print("\"Hello,\" he said.")

#Bildiğimiz gibi s değişkeni oluşturduk ve değer atadık.
#\n operatörü ile alt satıra inmemiz gerekmektedir.
s='\nIlk Satır.\nIkinci Satir. \nUcuncu Satir.'
print(s)


print('C:\some\name')# \ operatöünü normal kullanırsak name kelimesinde \n i yakalayıp alt satıra inecektir.
print(r'C:\some\name')# \ operatöünü r ile kullanırsak alt satıra inmeyecektir.

# """...""" veya '''...''' üçlü tırnak kullanırsak tırnaklar arasında nasıl yazdıysak o şekilde ekrana getirmektedir.
print("""\
Usage : thingy [OPTIONS]
        -h              Display this usage message
        -H hostname     Hostname to connect to
""")

print('''
        1
            2
                3
                    4
''')
#çıktı
#        1
#            2
#                3
#                    4

#String Birleştirme İşlemi + operatörü ile iki String ifadesini birleştirirken * operatörü ile o String ifadesini tekrarlayabiliyoruz.
print(3 * 'li' + 'HEY')

#iki String literali + operatörü hem kullanıp hem kullanmadan birleştirme işlemi yapabiliyoruz.
print('Py' 'thon')
print('Py' + 'thon')

#iki değerden biri literal olmasa işlemimiz hata verecektir.
#a='Py'
#print(a 'thon')
    #print(a 'thon')
     #           ^
#SyntaxError: invalid syntax


print('Baris Manco Nazo Gelin Ayagına Takar'
      'Hal Hal')

word='BESIKTAS'
print("word length = ", len(word))
print(word[0]+word[2]+word[4])
## print(word[11]) IndexError: string index out of range

print(word[-1],word[-2],word[-8]) # word[-1] Stringi içinde en son karakteri dönmektedir.
#print(word[-12]) string index out of range


print(word[0:2])
print(word[3:6])

print(word[:2]+word[2:])



print(word[4:35])

word='Y'+ word
print(word)

# LİST
#dizi tanımlamalarımızı [] braketler içinde tanımlıyoruz.
dizi = [1,2,4,8,16]
print(dizi)

print(dizi[0])# 0. indisdeki değeri getirecek

print(dizi[-1])# son indisteki değeri getirecek

print(dizi[2:4])# 2. indisten 4. indise kadar olan değerleri getirecek 4 dahil değil

dizi = dizi + [32,64,128,256] #diziyi kolayca birleştirebiliyoruz.
print(dizi)

dizi1= [1,8,27,65,125] # yanlış oluşturulmuş bir dizimiz olsun
print(dizi1)
dizi1[3] = 64 # aradaki bir değeri güncelleştirebiliyoruz. String ifade içinde bunu yapamamıştık.
print(dizi1)

dizi1.append(216) # append fonkiyonu ile dizimizin sonuna yeni değer ekleyebiliriz.
dizi1.append(7**3)
print(dizi1) # üs almak için ** operatörünü kullanabiliriz.

letters=['a','b','c','d','e','f','g','h']
print(letters)
letters[2:5]=['C','D','E'] # 2,3,4 indisdeki değerlerin yerine C,D,E değerleri gelecektir.
print(letters)
letters[2:5]=['c','d','e','X','Y','Z'] #letters dizisindeki 3 karakterin yerine 6 karakter yazarsak ne olacak?
print(letters) # letters dizisindeki ilk 2,3,4 indislerin yerine c,d,e gelirken X,Y,Z değerleri ise 4. indis ile 5. indis arasına girmektedir.
print(letters.index('X'),letters.index('Y'),letters.index('Z'))

#çoklu atama işlemleri
x=3
x,y=0,x # aynı satır üzerinde işlem yapsada öncelikle x değerini 0 yapıyor daha sonra y değerine x değerini atıyor


print('x = ',x,'y = ',y)

a,b=0,1
while b<10: #b<10 ifadesi doğru oldukça alttaki ifade çalışacaktır.Eğer başka programlama dilinde gördüysek kolayca anlaşılacaktır.
    print (b)
    a,b=b,a+b

a,b=0,1
while b<1000: #b<10 ifadesi doğru oldukça alttaki ifade çalışacaktır.Eğer başka programlama dilinde gördüysek kolayca anlaşılacaktır.
    print(b, end=',')
    a,b=b,a+b

