import pyodbc
import time

def checkTableExists(dbcon, tablename, schemaName):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.TABLES
        WHERE table_name = '{0}' and table_schema = '{1}'
        """.format(tablename, schemaName))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
    dbcur.close()
    return False

vt = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-32JOH3P\SQLEXPRESS;Database=proje;trusted_connection=yes")
imlec = vt.cursor()
varmi = checkTableExists(vt, 'deneme', 'dbo')

if varmi == False:
    imlec.execute(
                  ""
                  "CREATE TABLE "
                  "dbo.deneme (id INT NOT NULL IDENTITY PRIMARY KEY,"
                  "kitap_adi VARCHAR(50),"
                  "kitap_adedi INT,"
                  "kitap_yazari VARCHAR(50),"
                  "kitap_yayinevi VARCHAR(50),"
                  "kitap_fiyati INT )"
                  ""
                  )
    vt.commit()



def kitap_ekle():

    vt = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-32JOH3P\SQLEXPRESS;Database=proje;trusted_connection=yes")
    imlec = vt.cursor()

    kitap_adi = input("kitap adını giriniz : ")
    kitap_adedi = input("kitap adedi : ")
    kitap_yazari = input("kitap yazarı : ")
    kitap_yayinevi = input("kitap yayınevi : ")
    kitap_fiyati = input("kitap fiyatı : ")


    kitap_girisi = "INSERT INTO deneme (kitap_adi,kitap_adedi,kitap_yazari,kitap_yayinevi,kitap_fiyati) VALUES ('"+kitap_adi+"','"+kitap_adedi+"','"+kitap_yazari+"','"+kitap_yayinevi+"','"+kitap_fiyati+"')"

    imlec.execute(kitap_girisi)
    vt.commit()

def kitap_sil():
    vt = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-32JOH3P\SQLEXPRESS;Database=proje;trusted_connection=yes")
    imlec = vt.cursor()
    silinecek = input("Slinecek kitabın İD numarasını giriniz : ")

    imlec.execute("DELETE FROM deneme WHERE id = '" + silinecek + "'")
    vt.commit()

def kitap_listele():
    vt = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-32JOH3P\SQLEXPRESS;Database=proje;trusted_connection=yes")
    imlec = vt.cursor()

    imlec.execute("SELECT * FROM deneme")
    kitaplar = imlec.fetchall()


    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")


def kitapfiyati_guncelle():
    vt = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-32JOH3P\SQLEXPRESS;Database=proje;trusted_connection=yes")
    imlec = vt.cursor()

    yenifiyat = input("yeni fiyatı girin : ")
    kitapid = input("fiyatını değiştirmek istedğin id : ")
    imlec.execute("UPDATE deneme SET kitap_fiyati = '" + yenifiyat + "' WHERE id = '" + kitapid + "'")

    vt.commit()

def kitapadedi_guncelle():
    vt = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=DESKTOP-32JOH3P\SQLEXPRESS;Database=proje;trusted_connection=yes")
    imlec = vt.cursor()

    yeniadet = input("yeni adedi girin : ")
    kitapid = input("adedini değiştirmek istedğin id : ")
    imlec.execute("UPDATE deneme SET kitap_adedi = '" + yeniadet + "' WHERE id = '" + kitapid + "'")

    vt.commit()


while True:
    print("--------------------------------------------------------")
    print("""
    **************** ASEL KİTAPÇILIK *******************
    """)

    print("""
            1 - KİTAP EKLE
            2 - KİTAPLIĞIMI LİSTELE
            3 - KİTAP SİL
            4 - GÜNCELLE
            q - ÇIKIŞ
            """)


    işlem = input("YAPMAK İSTEDİĞİNİZ İŞLEM : ")

    if(işlem=="1"):
        kitap_listele()
        print("---------------")
        kitap_ekle()
        print("işleminiz yapılıyor...")
        time.sleep(0.5)
        print("kayıt başarılı")

    elif(işlem=="2"):
        kitap_listele()

    elif(işlem=="3"):
        kitap_listele()
        print("-------------")
        kitap_sil()
        print("işleminiz yapılıyor...")
        time.sleep(0.5)
        print("işlem başarılı")

    elif(işlem=="4"):
        kitap_listele()
        print("------------")
        print("""
            1- Fiyat güncelle
            2- Adedi Gncelle
        """)

        aded = input("işleminizi seçin : ")
        if(aded=="1"):
            kitapfiyati_guncelle()
        elif(aded=="2"):
            kitapadedi_guncelle()

    elif(işlem=="q" or işlem=="Q"):
        print("Çıkış yapılıyor.")
        time.sleep(0.5)
        break

    else:
        print("geçersiz işlem girdiniz...")









