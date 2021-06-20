# Hastane Randevu Sistemi

from datetime import datetime, date


class Hastane():
    def __init__(self,adi,adresi,bolumler,doktorlar):
        self.__adi=adi
        self.__adresi=adresi
        self.__bolumler=bolumler
        self.__doktorlar=doktorlar
        self.__rezervasyonlar=[]

    def getAdi(self):
        return self.__adi

    def setAdi(self,yeni_ad):
        self.__adi=yeni_ad
        print("Hastane adı değiştirildi...")

    def  getAdresi(self):
        return self.__adresi

    def setAdresi(self,yeni_adres):
        self.__adresi=yeni_adres
        print("Hastane adresi değiştirildi...")

    def getBolumler(self):
        print("==================Bölümlerimiz==================")
        for bolum in self.__bolumler:
            print("""
                    Bölüm :  {bolum}
                 
                 """.format(bolum=bolum))
            print("=" * 55)

    def bolumEkle(self,yeni_bolum):
        self.__bolumler.append(yeni_bolum)
        print("Bölüm eklendi......")


    def getDoktorlar(self):
        print("==================Doktorlarımız==================")
        for doktor in self.__doktorlar:
            print("""
                    İsim :  {isim}
                    Soyad :  {soyad}
                    Telefon :  {telefon}
                    Bolum :  {bolum}
                    
                 """.format(isim=doktor.getIsim(),soyad=doktor.getSoyad(),telefon=doktor.getTelefon(),bolum=doktor.getBolum()))
            print("=" * 55)

    def doktorEkle(self, yeni_doktor):
        self.__doktorlar.append(yeni_doktor)
        print("Doktor eklendi......")

    def rezervasyonYap(self,hasta,istenenDoktor,istenenTarih):
        müsaitlik=True
        for rezervasyon in self.__rezervasyonlar:
            listedeki_hasta=rezervasyon[0]
            listedeki_doktor = rezervasyon[1]
            listedeki_tarih= rezervasyon[2]

            if listedeki_doktor==istenenDoktor and listedeki_tarih==istenenTarih:
                print("Randevu tarihi müsait değildir, farklı tarihleri kontrol edin....")
                müsaitlik=False
        if müsaitlik:
            self.__rezervasyonlar.append((hasta,istenenDoktor,istenenTarih))
            print("Rezervasyon kaydı başarılı... Randevunuz alındı....")

    def getRezervasyonlar(self):
        print("="*60)
        print("====================Rezervasyonlar====================")
        rez_sayisi=0

        for rezervasyon in self.__rezervasyonlar:
            listedeki_hasta=rezervasyon[0]
            listedeki_doktor = rezervasyon[1]
            listedeki_tarih= rezervasyon[2]

            print("{hastaismi} {hastasoyadi} isimli hastanın {rez_tarihi} tarihinde Doktor {doktorismi} {doktorsoyad} ile randevusu vardır."
                  .format(hastaismi=listedeki_hasta.getIsim(),hastasoyadi=listedeki_hasta.getSoyad(),rez_tarihi=listedeki_tarih,doktorismi=listedeki_doktor.getIsim(),
                          doktorsoyad=listedeki_doktor.getSoyad()))
            print("="*60)
            rez_sayisi+=1
        if rez_sayisi == 0:
            print("Hiçbir rezervasyon yok..........")


class Birey():
    def __init__(self,isim,soyad,telefon):
        self.__isim=isim
        self.__soyad=soyad
        self.__telefon=telefon

    def getIsim(self):
        return self.__isim

    def getSoyad(self):
        return self.__soyad

    def getTelefon(self):
        return self.__telefon


class Doktor(Birey):

    doktor_sayisi=0

    def __init__(self,isim,soyad,telefon,bolum):
        super().__init__(isim,soyad,telefon)
        Doktor.doktor_sayisi_artir()
        self.__bolum=bolum

    def getBolum(self):
        return self.__bolum

    @classmethod
    def doktor_sayisi_artir(cls):
        cls.doktor_sayisi+=1

class Hasta(Birey):
    pass


d1=Doktor("Celal","İdemen","05424766376","Dahiliye")
d2=Doktor("Şeyma","Şafak","05424766376","Jinekolog")
d3=Doktor("Aydın","Gökşin","05424766376","Pratisyen")
d4=Doktor("Oguz","Tuncer","05424766376","Çocuk Uzmanı")

h1=Hasta("İsmail","Karasu","05435524935")
h2=Hasta("Nuray","Karasu","05304919934")

bolumler=["Dahiliye","Acil Tıp","Pratisyen","Cildiye","Jinekolog","Ürolog","Kardiyoloji"]

hastane=Hastane("Iğdır Devlet Hastanesi","Iğdır/Merkez",bolumler,[d1,d2,d3])

print("="*60)
print("{} Hastanesine hoşgeldinz.....".format(hastane.getAdi()))

# hastane.getBolumler()
# hastane.bolumEkle("Onkoloji")
# hastane.getBolumler()

# hastane.getDoktorlar()
# hastane.doktorEkle(d4)
# hastane.getDoktorlar()

hastane.getRezervasyonlar()

hastane.rezervasyonYap(h1,d1,date.today())
hastane.rezervasyonYap(h2,d1,date.today())

hastane.getRezervasyonlar()

print("Toplam Doktor Sayısı  :  ",Doktor.doktor_sayisi)