import csv
class Calisan:
    def __init__(self, isim, soyisim, calisan_id, departman, maas, izin_gunleri):
        self.isim = isim
        self.soyisim = soyisim
        self.calisan_id = calisan_id
        self.departman = departman
        self.maas = maas
        self.izin_gunleri = izin_gunleri

    def maas_guncelle(self, yeni_maas):
        """Çalışanın maaşını günceller."""
        self.maas = yeni_maas

    def zam_uygula(self, yuzde):
        """Çalışanın maaşına belirli bir yüzde oranında zam uygular."""
        self.maas += self.maas * (yuzde / 100)

    def izin_al(self, gun_sayisi):
        if gun_sayisi <= self.izin_gunleri:
            self.izin_gunleri -= gun_sayisi
            print(f"{gun_sayisi} gün izin aldiniz.Kalan izin günleriniz:{ self.izin_gunleri}")
        else:
            print("Yeterli izin gününüz yok!")
        def maas_guncelle(self, yeni_maas):
            self.maas = yeni_maas
            print(f"Maas güncellendi: {self.maas}")
class TamZamanli(Calisan):
    def __init__(self, isim, soyisim , calisan_id, departman, maas,):
       super().__init__(isim, soyisim, calisan_id, departman, maas, izin_gunleri=20)
class YariZamanli(Calisan):
    def __init__(self, isim, soyisim, calisan_id, departman, saatlik_ucret, calisma_saati):
        maas = saatlik_ucret * calisma_saati
        super().__init__(isim, soyisim, calisan_id,departman, maas, izin_gunleri=10)
class Calisan:
    def __init__(self, isim, soyisim, calisan_id, departman, proje_ucreti):
        super().__init__(isim, soyisim, calisan_id,departman, proje_ucreti, izin_gunleri=14)
class Yonetici:
    def __init__(self,isim,soyisim, calisan_id, departman, maas):
        super().__init__(isim, soyisim, calisan_id,departman,maas,izin_gunleri=14)
        self.yonetilenler = []
    def calisan_ekle(self,calisan):
        self.yonetilenler.append(calisan)
        print(f"{calisn.isim} {calisan.soyisim} yöneticinize eklendi.")
        for calisan in self.yonetilenler:
            print(f"- {calisan.isim} {calisan.soyisim}")

def csv_yukle(dosya_adi):
    calisanlar = []
    try:
        with open(dosya_adi, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    if row['CalisanTuru'] == 'TamZamanli':
                        calisan = TamZamanli(row['Isim'], row['Soyisim'], row['Calisan_ID'], row['Departman'],
                                            float(row['Maas']))
                    elif row['CalisanTuru'] == 'YariZamanli':
                        calisan = YariZamanli(row['Isim'],row['Soyisim'], row['CalisanID'], row['Departman'],
                                            float(row['ProjeUcreti']))
                    elif row['CalisanTuru'] == 'Danisman':
                        calisan = Danisman(row['Isim'], row['Soyisim'], row['CalisanID'],row['Departman'],
                                           float(row['ProjeUcreti']))
                    elif row['CalisanTuru'] == 'Yonetici':
                        calisan = Yonetici(row['Isim'], row['Soyisim'], row['CalisanID'], row['Departman'],
                                           float(row['Maas']))
                    else:
                        raise ValueError(f"Bilinmeyen çalışan türü: {row['CalisanTuru']}")
                    calisanlar.append(calisan)
                except KeyError as e:
                    print(f"Satırda eksik veri: {e}, Satır: {row}")
                except ValueError as e:
                    print(f"Veri hatası: {e}, Satır: {row}")
        print("Veriler yüklendi")
    except FileNotFoundError:
        print("CSV dosyası bulunamadı,yeni bir dosya oluşturulacak.")
    return calisanlar
def csv_kaydet(dosya_adi,calisanlar):
    with open(dosya_adi, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Isim', 'Soyisim', 'CalisanID', 'Departman', 'Maas', 'IzinGunleri', 'CalisanTuru', 'SaatlikUcret', 'CalismaSaati', 'ProjeUcreti']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for calisan in calisanlar:
            row = {
                'Isim': calisan.isim,
                'Soyisim': calisan.soyisim,
                'CalisanID': calisan.calisan_id,
                'Departman': calisan.departman,
                'Maas': calisan.maas,
                'IzinGunleri': calisan.izin_gunleri
            }
            if isinstance(calisan, TamZamanli):
                row['CalisanTuru'] = 'TamZamanli'
            elif isinstance(calisan, YariZamanli):
                row['CalisanTuru'] = 'YariZamanli'
                row['SaatlikUcret'] = calisan.maas / calisan.calisma_saati
                row['CalismaSaati'] = calisan.calisma_saati
            elif isinstance(calisan, Danisman):
                row['CalisanTuru'] = 'Danisman'
                row['ProjeUcreti'] = calisan.maas
            elif isinstance(calisan, Yonetici):
                row['CalisanTuru'] = 'Yonetici'
            writer.writerow(row)
        print("kaydedildi.")
if __name__ == "__main__":
    dosya_adi = "calisanlar.csv"
    calisan_listesi = csv_yukle(dosya_adi)
    yeni_calisan = TamZamanli("Elif","Çağlayan","777","Mühendislik",100000)
    calisan_listesi.append(yeni_calisan)
    csv_kaydet(dosya_adi, calisan_listesi)
    yeni_calisan.izin_al(5)
    yeni_calisan.maas_guncelle(150000)










