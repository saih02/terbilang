def hasil(num):
    huruf = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    if num < 12:
        temp = ' '+huruf[num]
    elif num < 20:
        temp = str(hasil(num-10))+' belas'
    elif num < 100:
        temp = str(hasil(num//10))+' puluh'+str(hasil(num%10))
    elif num < 200:
        temp = ' seratus'+str(hasil(num-100))
    elif num < 1000:
        temp = str(hasil(num//100))+' ratus'+str(hasil(num%100))
    elif num < 2000:
        temp = ' seribu'+str(hasil(num-1000))
    elif num < 1000000:
        temp = str(hasil(num//1000))+' ribu'+str(hasil(num%1000))
    elif num < 1000000000:
        temp = str(hasil(num//1000000))+' juta'+str(hasil(num%1000000))
    elif num < 1000000000000:
        temp = str(hasil(num//1000000000))+' milyar'+str(hasil(num%1000000000))
    elif num < 1000000000000000:
        temp = str(hasil(num//1000000000000))+' trilyun'+str(hasil(num%1000000000000))
    return temp

def terbilang(num):
    if num < 0:
        hasilV = 'minus '+hasil(num)
    else:
        hasilV = hasil(num)
    return hasilV