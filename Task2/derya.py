import csv

class Personel:
    def _init_(self, ad, soyad, id, departman, maas, izin_gunu):
        self.ad = ad
        self.soyad = soyad
        self.id = id
        self.departman = departman
        self.maas = maas
        self.izin_gunu = izin_gunu

    def maas_yenile(self, yeni_maas):
        self.maas = yeni_maas

    def zam(self, yuzde):
        self.maas += self.maas * (yuzde / 100)
    def izin(self, gun_sayisi):
        if gun_sayisi <= self.izin_gunu:
            self.izin_gunu -= gun_sayisi
            print(f"{gun_sayisi} izin aldınız. Kalan izin: {self.izin_gunu}")
        else:
            print("izin hakkınız kalmadı!")

class TamZamanli(Personel):
    def _init_(self, ad, soyad, id, departman, maas):
        super()._init_(ad, soyad, id, departman, maas, izin_gunleri=30)

class YariZamanli(Personel):
    def _init_(self, ad, soyad, id, departman, saatlik_ucret, calisma_saati):
        maas = saatlik_ucret * calisma_saati
        super()._init_(ad, soyad, id, departman, maas, izin_gunleri=10)

class Danisman(Personel):
    def _init_(self, ad, soyad, id, departman, proje_ucreti):
        super()._init_(ad, soyad, id, departman, proje_ucreti, izin_gunleri=14)

class Yonetici(Personel):
    def _init_(self, ad, soyad, id, departman, maas):
        super()._init_(ad, soyad, id, departman, maas, izin_gunleri=14)
        self.yonetilenler = []

    def personel_ekle(self, personel):
        self.yonetilenler.append(personel)
        print(f"{personel.ad} {personel.soyad} yönetime eklendi.")
        for personel_listesil in self.personeller:

def csv_yukle(dosya_adi):
    personeller = []
    try:
        with open(dosya_adi, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    if row['PersonelTuru'] == 'TamZamanli':
                        personel = TamZamanli(row['Ad'], row['Soyad'], row['PersonelID'], row['Departman'],
                                              float(row['Maas']))
                    elif row['PersonelTuru'] == 'YariZamanli':
                        personel = YariZamanli(row['Ad'], row['Soyad'], row['PersonelID'], row['Departman'],
                                               float(row['SaatlikUcret']), float(row['CalismaSaati']))
                    elif row['PersonelTuru'] == 'Danisman':
                        personel = Danisman(row['Ad'], row['Soyad'], row['PersonelID'], row['Departman'],
                                            float(row['ProjeUcreti']))
                    elif row['PersonelTuru'] == 'Yonetici':
                        personel = Yonetici(row['Ad'], row['Soyad'], row['PersonelID'], row['Departman'],
                                            float(row['Maas']))
                    else:
                        raise ValueError(f"Bilinmeyen personel türü: {row['PersonelTuru']}")
                    personeller.append(personel)
                except KeyError as e:
                    print(f"Satırda eksik veri: {e}, Satır: {row}")
                except ValueError as e:
                    print(f"Veri hatası: {e}, Satır: {row}")
        print("Veriler yüklendi.")
    except FileNotFoundError:
        print("CSV dosyası bulunamadı, yeni bir dosya oluşturulacak.")
    return personeller

def csv_kaydet(dosya_adi, personeller):
    with open(dosya_adi, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Ad', 'Soyad', 'PersonelID', 'Departman', 'Maas', 'IzinGunleri', 'PersonelTuru', 'SaatlikUcret', 'CalismaSaati', 'ProjeUcreti']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for personel in personeller:
            row = {
                'Ad': personel.ad,
                'Soyad': personel.soyad,
                'PersonelID': personel.personel_id,
                'Departman': personel.departman,
                'Maas': personel.maas,
                'IzinGunleri': personel.izin_gunleri
            }
            if isinstance(personel, TamZamanli):
                row['PersonelTuru'] = 'TamZamanli'
            elif isinstance(personel, YariZamanli):
                row['PersonelTuru'] = 'YariZamanli'
                row['SaatlikUcret'] = personel.maas / personel.calisma_saati
                row['CalismaSaati'] = personel.calisma_saati
            elif isinstance(personel, Danisman):
                row['PersonelTuru'] = 'Danisman'
                row['ProjeUcreti'] = personel.maas
            elif isinstance(personel, Yonetici):
                row['PersonelTuru'] = 'Yonetici'
            writer.writerow(row)
        print("Kaydedildi.")

if _ad_ == "_main_":
    dosya_adi = "personeller.csv"
    personel_listesi = csv_yukle(dosya_adi)
    yeni_personel = TamZamanli("ahmet", "demir", "345", "Mühendislik", 75000)
    personel_listesi.append(yeni_personel)
    csv_kaydet(dosya_adi, personel_listesi)
    yeni_personel.izin_al(15)
    yeni_personel.maas_guncelle(360000)
