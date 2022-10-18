import math

#Считает НДС(20%) для документов
def nds(number):
    nds=round(number/6,2)
    nds='{0:,}'.format(nds).replace(',', ' ')
    word=nds+' рублей'
    return word

#Выводит сумму для документов
def summa(number):
    float =int((number % 1)*100)
    if float==0:
        float='00'
    number_f=str(math.trunc(number))
    razryad='{0:,}'.format(int(number_f)).replace(',', ' ')
    if int(number_f[-1])==1:
        word= razryad+' ('+n2t(int(number_f))+') рубль '+str(float)+' копеек'
        return word
    elif 1<=int(number_f[-1])<=4:
        word = razryad + ' (' + n2t(int(number_f)) + ') рубля '+str(float)+' копеек'
        return word
    elif 4<int(number_f[-1])<=9 or int(number_f[-1])==0:
        word = razryad + ' (' + n2t(int(number_f)) + ') рублей '+str(float)+' копеек'
        return word

#Выводит число прописью(только int)
def n2t(number):
    def words(word):
        word = str(word).replace('[', '')
        word = word.replace(']', '')
        word = word.replace("'", '')
        word = word.replace(",", '')
        word = word.replace("   ", ' ')
        word = word.replace("  ", ' ')
        if word[-1] == ' ':
            word = word[:-1]
        return word
    #Библиотека
    one=['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять','десять']
    desyatki=['одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семьнадцать','восемьнадцать','девятнадцать']
    ten=['десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто','']
    hundred=['сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот','']
    thousend=['одна','две','три','четыре','пять','шесть','семь','восемь','девять','']

    #Переменные:

    #edenica-еденички
    #sotka-сотки
    #tysacha-тысячи
    #ten_tysacha-десять тысяч
    #thousend_tysacha-сто тысяч
    #million-миллион
    #ten_million-десятки миллионов
    #des-булево значение, используемое в случае, если число от 11 до 19


    word = []
    number_f=str(number)
    desyatok=False

    # Еденицы
    def a1(number_f, des):
        edenica = number_f[-1]
        if int(edenica)!=0 and des==False:
            word.append(one[int(edenica)])
        elif des==True:
            word.append('')
        return word

    # Десятки
    def a10(number_f):
        edenica = number_f[-1]
        desyatok = number_f[-2]
        des=False
        if 1<int(desyatok):
            a=word.append(ten[int(desyatok)-1])
            des=False
            return a1(number_f, des)
        elif int(desyatok)==1 and int(edenica)!=0:
            word.append(desyatki[int(edenica)-1])
            des=True
            return a1(number_f, des)
        elif int(desyatok)==0:
            des = False
            return a1(number_f, des)


    # Сотни
    def a100(number_f):
        edenica = number_f[-1]
        desyatok = number_f[-2]
        sotka = number_f[-3]
        if (int(sotka)) !=0:
            word.append(hundred[int(sotka)-1])
        return a10(number_f)

    # Тысячи
    def a1000(number_f):
        if int(number_f)<=9999:
            tysacha=number_f[-4]
            des = False
        else:
            tysacha = number_f[-4]
            ten_tysacha=number_f[-5]
            if int(tysacha)!=1 and int(ten_tysacha)==1:
                des=True
            else: des=False
        if int(tysacha)==1 and des!=True:
           word.append('одна тысяча')
        elif 1<int(tysacha)<=4 and des!=True:
            word.append(thousend[int(tysacha)-1]+' тысячи')
        elif 4<int(tysacha)<=9 and des!=True:
            word.append(thousend[int(tysacha) - 1] + ' тысяч')
        elif des==True:
             word.append('тысяч')
        elif (int(ten_tysacha)>1 and des!=True):
            word.append('тысяч')
        return a100(number_f)

    # Десятки тысяч
    def a10000(number_f):
        tysacha = number_f[-4]
        ten_tysacha=number_f[-5]
        if int(ten_tysacha)!=0 and int(tysacha)==0:
            word.append(ten[int(ten_tysacha)-1])
        elif int(ten_tysacha)==1 and int(tysacha)!=0:
            word.append(desyatki[int(tysacha) - 1])
        else:
            word.append(ten[int(ten_tysacha)-1])
        return a1000(number_f)

    # Сотни тысяч
    def a100000(number_f):
        thousend_tysacha=number_f[-6]
        if number-100000*int(thousend_tysacha)!=0:
           word.append(hundred[int(thousend_tysacha)-1])
        else:
            word.append(hundred[int(thousend_tysacha) - 1]+' тысяч')
        return a10000(number_f)

    # Миллионы
    def a1000000(number_f):
        if number<10000000:
            million=number_f[-7]
            des=False
        else:
            million = number_f[-7]
            ten_million = number_f[-8]
            if int(million)!=0 and int(ten_million)==1:
                des=True
            else:
                des=False

        if int(million)==1 and des==False:
            word.append(one[int(million)]+' миллион')
        elif 1<int(million)<=4 and des==False:
            word.append(one[int(million)] + ' миллионa')
        elif 4<int(million)<=9 and des==False:
            word.append(one[int(million)] + ' миллионов')
        else:
            word.append('миллионов')
        return a100000(number_f)
    # Десятки миллионов
    def a10000000(number_f):
        million = number_f[-7]
        ten_million=number_f[-8]
        if int(million) != 0 and int(ten_million) == 1:
            des = True
        else:
            des = False

        if des==True:
            word.append(desyatki[int(million)-1])
        else:
            word.append(ten[int(ten_million)-1])
        return a1000000(number_f)


    #Разбивает числа по разрядам
    if number<=10:
        return words(a1(number_f, des=False))
    elif 11<=number<=99:
        return words(a10(number_f))
    elif 100<=number<=999:
        return words(a100(number_f))
    elif 1000<=number<=9999:
        return words(a1000(number_f))
    elif 10000<=number<=99999:
        return words(a10000(number_f))
    elif 100000<=number<=999999:
        return words(a100000(number_f))
    elif 1000000<=number<=10000000:
        return words(a1000000(number_f))
    elif 10000000<number<100000000:
        return words(a10000000(number_f))
    else:
        return 'Error: На данный момент функция работает с числами до 99 999 999'
