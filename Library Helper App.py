#Projek UAS Algoritma dan Pemrograman 2
#William Susilo (56220008)
#Geraldo Tan (50220277)

#Sabtu, 1 Juli 2023

#Jangan Lupa untuk Install WConio2, PrettyTable

#Untuk Run Python Filenya, Terkhusus untuk Panel Position Terminalnya Dibuat ke Left atau Right supaya Saat Looping Tidak Ada Sisa
import os
import WConio2 as WConio

#MENDAPATKAN PATH SESUAI DENGAN SISTEM OPERASI 
if os.name == 'nt':  # Windows
    folder_path = r"C:\WILLIAM SUSILO-GERALDO TAN-ALGORITMA DAN PEMROGRAMAN 2-KELAS T (Codingan Python)\Output File TxT"
else:  # Linux
    folder_path = "/home/user/WILLIAM SUSILO-GERALDO TAN-ALGORITMA DAN PEMROGRAMAN 2-KELAS T (Codingan Python)/Output File TxT"

file_path = os.path.join(folder_path, "WILLIAM SUSILO-GERALDO TAN-ALGORITMA DAN PEMROGRAMAN 2-KELAS T (Codingan Python).txt")

#MEMBUAT FOLDER JIKA BELUM ADA
os.makedirs(folder_path, exist_ok=True)

selesai = False

nam = []
nom = []
hp = []
tang = []
bul = []
tah = []
k_buku = []
teng = []
tang_akh = []
bul_akh = []
tah_akh = []
ket = []
i = 0

#FUNCTION: CLEAR SCREEN
def clear_screen():
    os.system("cls")


#FUNCTION: MENU
def menu_utama():
    WConio.textcolor(WConio.LIGHTMAGENTA)
    print("Selamat Datang di App Helper Perpustakaan Kwik Kian Gie")
    print("=======================================================")
    WConio.textcolor(WConio.WHITE)
    print("1. Tentang")
    print("2. Mode Anggota Perpustakaan")
    print("3. Mode Staff Perpustakaan")
    WConio.textcolor(WConio.YELLOW)
    print("0. Keluar")
    print("")
    WConio.textcolor(WConio.WHITE)

def menu_tentang():
    WConio.textcolor(WConio.LIGHTGREEN)
    print("Tentang Kami")
    print("------------")
    WConio.textcolor(WConio.WHITE)
    print("")
    print("Aplikasi ini dibuat dengan tujuan untuk memudahkan seluruh lapisan anggota dan staff dari Perpustakaan Kwik Kian Gie.")
    print("Diharapkan dengan hadirnya aplikasi ini dapat memudahkan segala bentuk interaksi dan validasi yang dibutuhkan di dalamnya.")
    print("")

def menu_tentang_print(file):
    file.write("Tentang Kami\n")
    file.write("------------\n\n")
    file.write("Aplikasi ini dibuat dengan tujuan untuk memudahkan seluruh lapisan anggota dan staff dari Perpustakaan Kwik Kian Gie.\n")
    file.write("Diharapkan dengan hadirnya aplikasi ini dapat memudahkan segala bentuk interaksi dan validasi yang dibutuhkan di dalamnya.\n")

def menu_anggota():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Selamat Datang di Perpustakaan Kwik Kian Gie")
    print("============================================")
    WConio.textcolor(WConio.WHITE)
    print("1. Tentang Perpustakaan Kwik Kian Gie")
    print("2. Daftar Buku Yang Tersedia")
    print("3. Aksi Peminjaman Buku")
    print("4. Lihat Data Peminjaman Buku (+ Ditampilkan di File .txt)")
    print("5. Tentang Pengembalian Buku dan Lihat Denda")
    WConio.textcolor(WConio.YELLOW)
    print("0. Kembali ke Menu Utama")
    WConio.textcolor(WConio.WHITE)
    print("")

def mode_daftar_buku():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Mode Daftar Buku yang Tersedia")
    print("==============================")
    WConio.textcolor(WConio.WHITE)
    print("1. Daftar Buku Diurutkan Berdasarkan Rating (Insertion Sorting)")
    print("2. Daftar Buku Diurutkan Berdasarkan Penjualan Buku (Selection Sorting)")
    print("3. Daftar Buku Diurutkan Berdasarkan Tahun Edisi Buku (Bubble Sorting)")
    print("4. Pencarian Buku yang Tersedia")
    WConio.textcolor(WConio.YELLOW)
    print("0. Kembali ke Menu Utama")
    WConio.textcolor(WConio.WHITE)
    print("")

def mode_pencarian_buku():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Mode Pencarian Buku yang Tersedia")
    print("=================================")
    WConio.textcolor(WConio.WHITE)
    print("1. Pencarian Buku Berdasarkan Rating (Merge Sort dan Binary Search)")
    print("2. Pencarian Buku Berdasarkan Penjualan Buku (Selection Sort dan Binary Search)")
    print("3. Pencarian Buku Berdasarkan Tahun Edisi Buku (Selection Sort dan Interpolation Search)")
    WConio.textcolor(WConio.YELLOW)
    print("0. Kembali ke Mode Daftar Buku yang Tersedia")
    WConio.textcolor(WConio.WHITE)
    print("")

def menu_tentang_perpus():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Tentang Perpustakaan Kwik Kian Gie")
    print("----------------------------------")
    print("")
    WConio.textcolor(WConio.WHITE)
    print("Perpustakaan Institut Bisnis dan Informatika Kwik Kian Gie (IBI KKG)")
    print("didirikan bersama dengan organisasi induknya yaitu Institut Bisnis dan Informatika Kwik Kian Gie pada tahun 1987")
    print("Lokasi Perpustakaan IBI KKG bertempat di Jl. Yos Sudarso Kav.87 Sunter Jakarta Utara")
    print("")

def menu_tentang_perpus_print(file):
    file.write("Tentang Perpustakaan Kwik Kian Gie\n")
    file.write("----------------------------------\n\n")
    file.write("Perpustakaan Institut Bisnis dan Informatika Kwik Kian Gie (IBI KKG)\n")
    file.write("didirikan bersama dengan organisasi induknya yaitu Institut Bisnis dan Informatika Kwik Kian Gie pada tahun 1987\n")
    file.write("Lokasi Perpustakaan IBI KKG bertempat di Jl. Yos Sudarso Kav.87 Sunter Jakarta Utara\n")

def menu_pinjam_buku():
    WConio.textcolor(WConio.LIGHTBLUE)       
    print("Informasi")
    print("===========================================================================")
    WConio.textcolor(WConio.LIGHTRED)
    print("Kartu NIM Anda Akan Ditahan Oleh Staff Sebagai Jaminan Buku yang Dipinjam ! ")
    WConio.textcolor(WConio.LIGHTBLUE)
    print("===========================================================================")
    print("")
    WConio.textcolor(WConio.WHITE)
    print("Tarif Denda Sebesar Rp.10.000,00 untuk Keterlambatan Pengembalian Buku Per 1 Hari ! ")
    print("")
    WConio.textcolor(WConio.YELLOW)
    print("Klik Enter untuk Melanjutkan Aksi Peminjaman Buku ! ")
    WConio.textcolor(WConio.WHITE)

def menu_staff():
    WConio.textcolor(WConio.LIGHTGREEN)
    print("       Staff Perpustakaan Kwik Kian Gie        ")
    WConio.textcolor(WConio.WHITE)
    print("===============================================")
    WConio.textcolor(WConio.LIGHTRED)
    print("   Input Angka 0 untuk Kembali ke Menu Utama   ")
    WConio.textcolor(WConio.WHITE)
    print("   -----------------------------------------   ")
    print("Clue = Masukkan Nomor Dosen Pak Fikri ! (99261)")
    WConio.textcolor(WConio.LIGHTGREEN)
    print("===============================================")
    WConio.textcolor(WConio.WHITE)
    verifikasi = input("Masukkan Nomor Induk Staff Perpustakaan = ")
    return verifikasi


#FUNCTION: PENGELOLAAN DAN PENCARIAN BUKU
def judul_buku():
    return ["Pengantar Bisnis                    || Kode = 105", \
            "Algoritma dan Pemrograman 1         || Kode = 111", \
            "Logika Informatika                  || Kode = 129", \
            "Matematika Informatika              || Kode = 123", \
            "Infrastruktur Teknologi Informasi   || Kode = 117", \
            
            "Bahasa Inggris                      || Kode = 102", \
            "Pendidikan Pancasila                || Kode = 108", \
            "Pendidikan Agama                    || Kode = 120", \
            "Arsitektur dan Organisasi Komputer  || Kode = 126", \
            "Algoritma dan Pemrograman 2         || Kode = 114", \
            
            "Statistika Bisnis                   || Kode = 121", \
            "Kalkulus 1                          || Kode = 109", \
            "Teknologi Informasi                 || Kode = 115", \
            "Struktur Data                       || Kode = 103", \
            "Pengantar Manajemen                 || Kode = 127", \
            
            "Pendidikan Kewarganegaraan          || Kode = 106", \
            "Sistem Operasi                      || Kode = 118", \
            "Analisis dan Perancangan Algoritma  || Kode = 112", \
            "E-Business                          || Kode = 130", \
            "Sistem Basis Data                   || Kode = 124", \
                
            "Teknik Kompilasi                    || Kode = 101", \
            "Data Mining                         || Kode = 107", \
            "Jaringan Komputer                   || Kode = 113", \
            "Pemrograman Web                     || Kode = 125", \
            "Web Technology 1                    || Kode = 119", \
            
            "Rekayasa Peranti Lunak              || Kode = 104", \
            "Web Technology 2                    || Kode = 116", \
            "Kalkulus 2                          || Kode = 122", \
            "Bahasa Indonesia                    || Kode = 128", \
            "Data Warehouse                      || Kode = 110"]
    
    #PENGIMPLEMENTASIAN INSERTION SORTING
def buku_rating(nama_buku, rating): 
    for i in range(len(nama_buku)-1):
        for j in range((i + 1), 0, -1): 
            variabel1 = nama_buku[j-1], rating[j-1]
            variabel2 = nama_buku[j], rating[j]
            if rating[j] < rating[j-1]:
                nama_buku[j-1], rating[j-1] = variabel2
                nama_buku[j], rating[j] = variabel1
    return nama_buku, rating

def urut_rating():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Daftar Buku Diurutkan Berdasarkan Rating")
    print("========================================")
    print("")
    WConio.textcolor(WConio.WHITE)
    
    nama_buku = judul_buku()
    rating = [3.8, 4.2, 3.5, 4.0, 4.5, \
              5.0, 3.1, 4.9, 2.9, 3.0, \
                
              4.7, 2.5, 3.9, 2.7, 4.1, \
              4.8, 2.8, 3.3, 4.6, 2.1, \
              
              3.7, 2.3, 3.4, 2.0, 2.2, \
              2.6, 2.4, 3.6, 4.4, 4.3]
    
    nama_buku_terurut, rating_terurut = buku_rating(nama_buku, rating)
    for i in range(len(nama_buku_terurut)):
        print(f"{i + 1}. {nama_buku_terurut[i]} || Rating: {rating_terurut[i]}")

def urut_rating_print(file):
    file.write("Daftar Buku Diurutkan Berdasarkan Rating\n")
    file.write("========================================\n")

    nama_buku = judul_buku()
    rating = [3.8, 4.2, 3.5, 4.0, 4.5, \
              5.0, 3.1, 4.9, 2.9, 3.0, \
                
              4.7, 2.5, 3.9, 2.7, 4.1, \
              4.8, 2.8, 3.3, 4.6, 2.1, \
              
              3.7, 2.3, 3.4, 2.0, 2.2, \
              2.6, 2.4, 3.6, 4.4, 4.3]

    nama_buku_terurut, rating_terurut = buku_rating(nama_buku, rating)
    for i in range(len(nama_buku_terurut)):
        file.write(f"{i + 1}. {nama_buku_terurut[i]} || Rating: {rating_terurut[i]} \n")
    file.write("\n")

    #PENGIMPLEMENTASIAN SELECTION SORTING
def penjualan_buku(nama_buku, jumlah_penjualan):
    for i in range (len(nama_buku)):
        nilai_akhir = i
        for j in range (i + 1, len(nama_buku)):
            if jumlah_penjualan[j] < jumlah_penjualan[nilai_akhir]:
                nilai_akhir = j
        nama_buku[i], nama_buku[nilai_akhir] = nama_buku[nilai_akhir], nama_buku[i]
        jumlah_penjualan[i], jumlah_penjualan[nilai_akhir] = jumlah_penjualan[nilai_akhir], jumlah_penjualan[i]
    return nama_buku, jumlah_penjualan

def urut_penjualan():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Daftar Buku Diurutkan Berdasarkan Jumlah Penjualan Buku")
    print("=======================================================")
    print("")
    WConio.textcolor(WConio.WHITE)
    
    nama_buku = judul_buku()
    jumlah_penjualan = [287, 391, 227, 336, 434, \
                        500, 135, 478, 93, 127, \
                        
                        412, 62, 354, 54, 382, \
                        444, 71, 312, 401, 12, \
                        
                        276, 32, 265, 11, 22, \
                        41, 17, 308, 418, 404]
    
    nama_buku_terurut, jumlahpenjualan_terurut = penjualan_buku(nama_buku, jumlah_penjualan)
    for i in range(len(nama_buku_terurut)):
        print(f"{i + 1}. {nama_buku_terurut[i]} || Penjualan: {jumlahpenjualan_terurut[i]}")

def urut_penjualan_print(file):
    file.write("Daftar Buku Diurutkan Berdasarkan Jumlah Penjualan Buku\n")
    file.write("=======================================================\n")

    nama_buku = judul_buku()
    jumlah_penjualan = [287, 391, 227, 336, 434, \
                        500, 135, 478, 93, 127, \
                        
                        412, 62, 354, 54, 382, \
                        444, 71, 312, 401, 12, \
                        
                        276, 32, 265, 11, 22, \
                        41, 17, 308, 418, 404]
    
    nama_buku_terurut, jumlahpenjualan_terurut = penjualan_buku(nama_buku, jumlah_penjualan)
    for i in range(len(nama_buku_terurut)):
        file.write(f"{i + 1}. {nama_buku_terurut[i]} || Penjualan: {jumlahpenjualan_terurut[i]} \n")
    file.write("\n")

    #PENGIMPLEMENTASIAN BUBBLE SORTING
def tahun_edisi_buku(nama_buku, tahun_buku):
    i = 0
    while i < (len(nama_buku)):
        j = 0
        while j < (len(nama_buku) - i - 1):
            variabel1 = nama_buku[j], tahun_buku[j]
            variabel2 = nama_buku[j+1], tahun_buku[j+1]
            if tahun_buku[j] > tahun_buku[j+1]:
                nama_buku[j+1], tahun_buku[j+1] = variabel1
                nama_buku[j], tahun_buku[j] = variabel2
            j += 1
        i += 1
    return nama_buku, tahun_buku

def urut_tahun():
    WConio.textcolor(WConio.LIGHTBLUE)
    print("Daftar Buku Diurutkan Berdasarkan Tahun Edisi Buku")
    print("==================================================")
    print("")
    WConio.textcolor(WConio.WHITE)
    
    nama_buku = judul_buku()
    tahun_buku = [2005, 1993, 1999, 2002, 2010, \
                  1995, 2008, 2001, 1992, 2009, \
                    
                  2006, 2003, 2007, 1994, 1997, \
                  1998, 1996, 2004, 2000, 2011, \
                    
                  1991, 2012, 2020, 2015, 2018, \
                  2016, 2013, 2017, 2014, 2019]
    
    nama_buku_terurut, tahunbuku_terurut = tahun_edisi_buku(nama_buku, tahun_buku)
    for i in range(len(nama_buku_terurut)):
        print(f"{i + 1}. {nama_buku_terurut[i]} || Tahun Edisi Buku: {tahunbuku_terurut[i]}")

def urut_tahun_print(file):
    file.write("Daftar Buku Diurutkan Berdasarkan Tahun Edisi Buku\n")
    file.write("==================================================\n")

    nama_buku = judul_buku()
    tahun_buku = [2005, 1993, 1999, 2002, 2010, \
                  1995, 2008, 2001, 1992, 2009, \
                    
                  2006, 2003, 2007, 1994, 1997, \
                  1998, 1996, 2004, 2000, 2011, \
                    
                  1991, 2012, 2020, 2015, 2018, \
                  2016, 2013, 2017, 2014, 2019]
    
    nama_buku_terurut, tahunbuku_terurut = tahun_edisi_buku(nama_buku, tahun_buku)
    for i in range(len(nama_buku_terurut)):
        file.write(f"{i + 1}. {nama_buku_terurut[i]} || Tahun Edisi Buku: {tahunbuku_terurut[i]} \n")
    file.write("\n")

    #PENGIMPLEMENTASIAN MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

    #PENGIMPLEMENTASIAN SELECTION SORTING
def selection_sorting(var):
    i = 0
    while i < (len(var)) - 1:
        nilai_akhir = i
        j = i + 1
        while j < (len(var)):
            if var[j] < var[nilai_akhir]:
                nilai_akhir = j
            j += 1
        var[i], var[nilai_akhir] = var[nilai_akhir], var[i]
        i += 1
    return var

    #PENGIMPLEMENTASIAN BINARY SEARCHING
def binary_searching(target, sorted_var):
    index = -1
    index1 = -1
    loop = 0
    low = 0
    high = len(sorted_var) - 1

    while high >= low:
        mid = (low + high) // 2
        loop += 1
        if float(sorted_var[mid]) == float(target):
            index = mid
            index1 = 0
            break
        elif float(sorted_var[mid]) < float(target):
            low = mid + 1
        else:
            high = mid - 1

    return index, index1

    #PENGIMPLEMENTASIAN INTERPOLATION SEARCHING
def interpolation_searching(target, sorted_bookcode):
    index = -1
    index1 = -1
    loop = 0

    low = 0
    high = len(sorted_bookcode) - 1
    kondisi = not False

    while high >= low and kondisi:
        loop += 1
        pembilang_pos = (int(target) - int(sorted_bookcode[low])) * (high - low)
        penyebut_pos = (int(sorted_bookcode[high]) - int(sorted_bookcode[low]))
        total_pos = low + (pembilang_pos // penyebut_pos)

        if total_pos >= (len(sorted_bookcode)) or total_pos < 0:
            break
        elif sorted_bookcode[total_pos] == target:
            index = total_pos
            index1 = 0
            kondisi = False
        elif sorted_bookcode[total_pos] < target:
            low = total_pos + 1
        elif sorted_bookcode[total_pos] > target:
            high = total_pos - 1

    return index, index1


#FUNCTION: PENGINPUTAN ANGGOTA PERPUSTAKAAN
def validasi_tanpa_angka(nama):
    valid = True
    for karakter in nama:
        if karakter >= '0' and karakter <= '9':
            valid = False
            break
    return valid

def input_nama():
    nama = input("Nama (2 Nama Terdepan Saja !) = ")
    while nama == " " or nama == "":
        os.system('cls')
        WConio.textcolor(WConio.LIGHTRED)
        print("Nama Harus Diisi ! ")
        print("")
        WConio.textcolor(WConio.WHITE)
        nama = input("Nama (2 Nama Terdepan Saja !) = ")
        while validasi_tanpa_angka(nama) == False:
            os.system('cls') 
            WConio.textcolor(WConio.LIGHTRED)
            print("Nama Diisi dengan Huruf Semuanya ! ")
            print("")            
            WConio.textcolor(WConio.WHITE)               
            nama = input("Nama (2 Nama Terdepan Saja !) = ")
    while validasi_tanpa_angka(nama) == False:
        os.system('cls')
        WConio.textcolor(WConio.LIGHTRED)
        print("Nama Diisi dengan Huruf Semuanya ! ")
        print("")   
        WConio.textcolor(WConio.WHITE)
        nama = input("Nama (2 Nama Terdepan Saja !) = ")
        while nama == " " or nama == "":
            os.system('cls')
            WConio.textcolor(WConio.LIGHTRED)
            print("Nama Harus Diisi ! ")
            print("")
            WConio.textcolor(WConio.WHITE)
            nama = input("Nama (2 Nama Terdepan Saja !) = ")
    print("")
    nam.append(nama)
    return nam

def input_nim():
    while True:
        os.system("cls")
        try:
            nim = int(input("NIM (Masukkan Angka !) = "))
            nim = str(nim)
            while len(nim) != 8:
                os.system('cls')
                WConio.textcolor(WConio.LIGHTRED)
                print("NIM Harus Berjumlah 8 Digit ! ")
                print("")
                WConio.textcolor(WConio.WHITE)
                nim = int(input("NIM (Masukkan Angka !) = "))
                print("")
                nim = str(nim)
            nom.append(nim)
            break
        except ValueError:
            print("")
            WConio.textcolor(WConio.LIGHTRED)
            print("------------------------------")
            print("NIM Harus Diisi dengan Angka !")
            print("")
            WConio.textcolor(WConio.YELLOW)
            print("Klik Enter untuk Memasukkan NIM Baru yang Sesuai!")
            WConio.textcolor(WConio.WHITE)
            enter = input()
        print("")
    print("")
    return nom

def input_handphone():
    while True:
        os.system("cls")
        try:
            no_hp = int(input("No. Handphone (Masukkan Angka Dimulai dari 0 !) = "))
            no_hp = str(no_hp)
            while len(no_hp) < 10 or len(no_hp) > 13:
                os.system('cls')
                WConio.textcolor(WConio.LIGHTRED)
                print("No. Handphone Berjumlah 10-13 Digit ! ")
                print("")
                WConio.textcolor(WConio.WHITE)
                no_hp = int(input("No. Handphone (Masukkan Angka Dimulai dari 0 !) = "))
                print("")
                no_hp = str(no_hp)
            hp.append(no_hp)
            break
        except ValueError:
            print("")
            WConio.textcolor(WConio.LIGHTRED)
            print("----------------------------------------")
            print("No. Handphone Harus Diisi dengan Angka !")
            print("")
            WConio.textcolor(WConio.YELLOW)
            print("Klik Enter untuk Memasukkan No. Handphone Baru yang Sesuai !")
            WConio.textcolor(WConio.WHITE)
            enter = input()
        print("")
    print("")
    return hp

def input_kodebuku():
    while True:
        os.system("cls")
        try:
            k_buk = int(input("Kode Buku yang Dipinjam = "))
            k_buk = str(k_buk)

            while (len(k_buk) != 3) or (k_buk != "101" and k_buk != "102" and k_buk != "103" and k_buk != "104" and k_buk != "105" \
                                        and k_buk != "106" and k_buk != "107" and k_buk != "108" and k_buk != "109" and k_buk != "110" \
                                        and k_buk != "111" and k_buk != "112" and k_buk != "113" and k_buk != "114" and k_buk != "115" \
                                        and k_buk != "116" and k_buk != "117" and k_buk != "118" and k_buk != "119" and k_buk != "120" \
                                        and k_buk != "121" and k_buk != "122" and k_buk != "123" and k_buk != "124" and k_buk != "125" \
                                        and k_buk != "126" and k_buk != "127" and k_buk != "128" and k_buk != "129" and k_buk != "130") :
                os.system('cls')
                WConio.textcolor(WConio.LIGHTRED)
                print("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! ")
                print("")
                WConio.textcolor(WConio.LIGHTBLUE)
                print("Daftar Buku yang Tersedia")
                print("=========================")
                WConio.textcolor(WConio.WHITE)
                print("1.  Pengantar Bisnis                    || Kode = 105")
                print("2.  Algoritma dan Pemrograman 1         || Kode = 111")
                print("3.  Logika Informatika                  || Kode = 129")
                print("4.  Matematika Informatika              || Kode = 123")
                print("5.  Infrastruktur Teknologi Informasi   || Kode = 117")
                
                print("6.  Bahasa Inggris                      || Kode = 102")
                print("7.  Pendidikan Pancasila                || Kode = 108")
                print("8.  Pendidikan Agama                    || Kode = 120")
                print("9.  Arsitektur dan Organisasi Komputer  || Kode = 126")
                print("10. Algoritma dan Pemrograman 2         || Kode = 114")
                
                print("11. Statistika Bisnis                   || Kode = 121")
                print("12. Kalkulus 1                          || Kode = 109")
                print("13. Teknologi Informasi                 || Kode = 115")
                print("14. Struktur Data                       || Kode = 103")
                print("15. Pengantar Manajemen                 || Kode = 127")
                 
                print("16. Pendidikan Kewarganegaraan          || Kode = 106")
                print("17. Sistem Operasi                      || Kode = 118")
                print("18. Analisis dan Perancangan Algoritma  || Kode = 112")
                print("19. E-Business                          || Kode = 130")
                print("20. Sistem Basis Data                   || Kode = 124")
                    
                print("21. Teknik Kompilasi                    || Kode = 101")
                print("22. Data Mining                         || Kode = 107")
                print("23. Jaringan Komputer                   || Kode = 113")
                print("24. Pemrograman Web                     || Kode = 125")
                print("25. Web Technology 1                    || Kode = 119")
                
                print("26. Rekayasa Peranti Lunak              || Kode = 104")
                print("27. Web Technology 2                    || Kode = 116")
                print("28. Kalkulus 2                          || Kode = 122")
                print("29. Bahasa Indonesia                    || Kode = 128")
                print("30. Data Warehouse                      || Kode = 110")
                print("")     

                WConio.textcolor(WConio.LIGHTRED) 
                print("Kode Harus Berjumlah 3 Digit Diawali Angka 1 ! ")
                print("")
                WConio.textcolor(WConio.WHITE)
                k_buk = int(input("Kode Buku yang Dipinjam = "))
                print("")
                k_buk = str(k_buk)                                
            break
        
        except ValueError:
            print("")
            WConio.textcolor(WConio.LIGHTRED)
            print("--------------------------------------------")
            print("Masukkan Kode Berupa Angka Diawali Angka 1 !")
            print("")
            WConio.textcolor(WConio.YELLOW)
            print("Klik Enter untuk Memasukkan Kode Buku Baru yang Sesuai !")
            WConio.textcolor(WConio.WHITE)
            enter = input()
        print("")
    print("")
    k_buku.append(k_buk)
    return k_buku


#FUNCTION: DIBAGIAN STAFF PENCARIAN DATA PEMINJAMAN BUKU
    #PENGIMPLEMENTASIAN SEQUENTIAL SEARCHING
def sequential_searching(cari, var):
    index = []
    index1 = -1
    loop = 0
    a = 0
    while a < len(var):
        if var[a] == cari:
            index.append(a)
            index1 = 0
        a += 1
        loop += 1
    return index, index1


#FUNCTION: KESALAHAN PENGINPUTAN
def opsi5_anggota(tang_akh):
    if tang_akh == []:
        WConio.textcolor(WConio.LIGHTRED)
        print("Belum Ada yang Melakukan Aksi Peminjaman Buku !")
        print("")
        WConio.textcolor(WConio.YELLOW)
        print("Klik Enter untuk Kembali ke Halaman Utama Mode Anggota Perpustakaan ! ")
        WConio.textcolor(WConio.WHITE)
    else:
        WConio.textcolor(WConio.LIGHTRED)
        print("Bagian Menu Ini Hanya Menampilkan Tampilan Informasi sebagai Berikut !")
        print("======================================================================")
        print("")
        print("Hubungi Staff Perpustakaan untuk Mengembalikkan Buku Pinjaman dan Melihat Jumlah Denda ! ")  
        print("")
        WConio.textcolor(WConio.YELLOW)
        print("Klik Enter untuk Kembali ke Halaman Utama Mode Anggota Perpustakaan ! ") 
        WConio.textcolor(WConio.WHITE)

def salahmode_anggota():
    WConio.textcolor(WConio.LIGHTRED)
    print("Tidak Valid ! ")
    print("")
    print("Silahkan Masukkan Angka Sesuai dengan Pilihan yang Disediakan ! ")
    print("")
    WConio.textcolor(WConio.YELLOW)
    print("Klik Enter untuk Melanjutkan Aksi ! ")
    WConio.textcolor(WConio.WHITE)

def salahmode_staff():
    WConio.textcolor(WConio.LIGHTRED)
    print("Tidak Valid ! ")
    print("")
    print("Silahkan Masukkan Angka Sesuai dengan Pilihan yang Disediakan ! ")
    print("")
    WConio.textcolor(WConio.YELLOW)
    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")

def salahmode_menuutama():
    WConio.textcolor(WConio.LIGHTRED)
    print("Tidak Valid ! ")
    print("")
    print("Silahkan Masukkan Angka Sesuai dengan Pilihan yang Disediakan ! ")
    print("")
    WConio.textcolor(WConio.YELLOW)
    print("Klik Enter untuk Melanjutkan Aksi ! ")

def salahkode_staff():
    WConio.textcolor(WConio.LIGHTRED)
    print("Nomor Induk yang Anda Masukkan Salah ! ")
    print("")
    print("Silahkan Masukkan Kembali Nomor Induk yang Benar ! ")
    print("")
    WConio.textcolor(WConio.YELLOW)
    print("Klik Enter untuk Melanjutkan Aksi ! ")
    WConio.textcolor(WConio.WHITE)

#################################################################

#PEMISAH UNTUK MENU UTAMA
while not selesai:
    os.system("cls")  
    menu_utama()
    pilihan_1 = input("Pilih ? ") 
    os.system("cls")

    if pilihan_1 == "1":
        os.system("cls")
        menu_tentang()
        with open(file_path, "w") as file:
            menu_tentang_print(file)
        WConio.textcolor(WConio.WHITE)
        print("===================================================")
        print("")
        WConio.textcolor(WConio.LIGHTRED)
        print("Hasil Output juga Ditampilkan pada File .txt ! ")
        print("")
        WConio.textcolor(WConio.YELLOW)
        print("Klik Enter untuk Kembali ke Menu Utama ! ")
        enter = input()

#PEMISAH UNTUK ANGGOTA PERPUSTAKAAN
    elif pilihan_1 == "2":  
        while True:
            os.system("cls")
            menu_anggota()

            pilihan = input("Pilih ? ") 
            os.system("cls")

            if pilihan == "1":
                os.system("cls")
                menu_tentang_perpus()
                with open(file_path, "w") as file:
                    menu_tentang_perpus_print(file)
                WConio.textcolor(WConio.WHITE)
                print("===================================================")
                print("")
                WConio.textcolor(WConio.LIGHTRED)
                print("Hasil Output juga Ditampilkan pada File .txt ! ")
                print("")
                WConio.textcolor(WConio.YELLOW)
                print("Klik Enter untuk Kembali ke Halaman Utama Mode Anggota Perpustakaan ! ")
                enter = input()
            
            elif pilihan == "2":
                os.system("cls")   
                while True:
                    os.system("cls")
                    mode_daftar_buku()

                    pilihan_2 = input("Pilih ? ")
                    os.system("cls")

                    #PENGIMPLEMENTASIAN INSERTION SORTING
                    if pilihan_2 == "1":
                        os.system('cls')
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! ")
                        print("")
                        urut_rating()
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Hafalkan Kode Buku yang Dituju untuk Aksi Peminjaman Buku ! ")
                        print("")
                        
                        with open(file_path, "w") as file:
                            file.write("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! \n\n")
                            urut_rating_print(file)
                            file.write("Hafalkan Kode Buku yang Dituju untuk Aksi Peminjaman Buku ! \n")
                        
                        WConio.textcolor(WConio.WHITE)
                        print("===================================================")
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Hasil Output juga Ditampilkan pada File .txt ! ")
                        print("")
                        WConio.textcolor(WConio.YELLOW)
                        print("Klik Enter untuk Kembali ke Halaman Utama Mode Daftar Buku yang Tersedia ! ")
                        enter = input()

                    #PENGIMPLEMENTASIAN SELECTION SORTING
                    elif pilihan_2 == "2":
                        os.system('cls')
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! ")
                        print("")
                        urut_penjualan()
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Hafalkan Kode Buku yang Dituju untuk Aksi Peminjaman Buku ! ")
                        print("")

                        with open(file_path, "w") as file:
                            file.write("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! \n\n")
                            urut_penjualan_print(file)
                            file.write("Hafalkan Kode Buku yang Dituju untuk Aksi Peminjaman Buku ! \n")

                        WConio.textcolor(WConio.WHITE)
                        print("===================================================")
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Hasil Output juga Ditampilkan pada File .txt ! ")
                        print("")
                        WConio.textcolor(WConio.YELLOW)
                        print("Klik Enter untuk Kembali ke Halaman Utama Mode Daftar Buku yang Tersedia ! ")
                        enter = input()

                    #PENGIMPLEMENTASIAN BUBBLE SORTING
                    elif pilihan_2 == "3":
                        os.system('cls')
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! ")
                        print("")
                        urut_tahun()
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Hafalkan Kode Buku yang Dituju untuk Aksi Peminjaman Buku ! ")
                        print("")

                        with open(file_path, "w") as file:
                            file.write("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! \n\n")
                            urut_tahun_print(file)
                            file.write("Hafalkan Kode Buku yang Dituju untuk Aksi Peminjaman Buku ! \n")

                        WConio.textcolor(WConio.WHITE)
                        print("===================================================")
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Hasil Output juga Ditampilkan pada File .txt ! ")
                        print("")
                        WConio.textcolor(WConio.YELLOW)
                        print("Klik Enter untuk Kembali ke Halaman Utama Mode Daftar Buku yang Tersedia ! ")
                        enter = input()

                    elif pilihan_2 == "4":
                        while True:
                            os.system("cls")
                            mode_pencarian_buku()

                            pilihan_4 = input("Pilih ? ")
                            os.system("cls")

                            #PENGIMPLEMENTASIAN MERGE SORT DAN BINARY SEARCHING
                            if pilihan_4 == "1":
                                rating = [3.8, 4.2, 3.5, 4.0, 4.5, \
                                          5.0, 3.1, 4.9, 2.9, 3.0, \
                                                
                                          4.7, 2.5, 3.9, 2.7, 4.1, \
                                          4.8, 2.8, 3.3, 4.6, 2.1, \
                                            
                                          3.7, 2.3, 3.4, 2.0, 2.2, \
                                          2.6, 2.4, 3.6, 4.4, 4.3]

                                sorted_rating = merge_sort(rating)

                                while True:
                                    try:
                                        os.system('cls')
                                        WConio.textcolor(WConio.LIGHTBLUE)
                                        print("Pencarian Buku Berdasarkan Rating")
                                        print("=================================")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("Perhatikan Angka yang Diinput Akan Berpengaruh pada Pencarian!")
                                        WConio.textcolor(WConio.WHITE)
                                        print("")
                                        cari_buku_rating = float(input("Masukkan Rating Buku yang Ingin Dicari = "))
                                        break
                                    except ValueError:
                                        print("")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("------------------------------")
                                        print("Input Harus Diisi dengan Angka !")
                                        print("")
                                        WConio.textcolor(WConio.YELLOW)
                                        print("Klik Enter untuk Memasukkan Input Baru yang Sesuai!")
                                        WConio.textcolor(WConio.WHITE)
                                        enter = input()
                                        os.system('cls')
                                    print("")
                                print("")
                                
                                index, index1 = binary_searching(cari_buku_rating, sorted_rating)

                                if index1 != -1:
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Buku dengan Rating =", cari_buku_rating, "Ditemukan!")
                                    print("")
                                    WConio.textcolor(WConio.WHITE)
                                    print("=============================")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Berikut Ini Tampilan Datanya!")
                                    print("")
                                    nama_buku = judul_buku()
                                    WConio.textcolor(WConio.WHITE)

                                    rating1 = [3.8, 4.2, 3.5, 4.0, 4.5, \
                                          5.0, 3.1, 4.9, 2.9, 3.0, \
                                                
                                          4.7, 2.5, 3.9, 2.7, 4.1, \
                                          4.8, 2.8, 3.3, 4.6, 2.1, \
                                            
                                          3.7, 2.3, 3.4, 2.0, 2.2, \
                                          2.6, 2.4, 3.6, 4.4, 4.3]
                        
                                    namabuku, hasilrating = buku_rating(nama_buku, rating1)

                                    print(f"{namabuku[index]} || Rating: {sorted_rating[index]}")
                                    print("")

                                    with open(file_path, "w") as file:
                                        file.write("Buku dengan Rating = "+ str(cari_buku_rating) + " Ditemukan! \n\n")
                                        file.write("=============================\n")
                                        file.write("Berikut Ini Tampilan Datanya!\n\n")
                                        file.write(f"{namabuku[index]} || Rating: {sorted_rating[index]}\n")

                                    WConio.textcolor(WConio.WHITE)
                                    print("===================================================")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Mode Pencarian Buku ! ")

                                else:
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Buku dengan Rating =", cari_buku_rating, "Tidak Ditemukan!")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("")
                                    print("Klik Enter untuk Kembali ke Mode Pencarian Buku ! ")
                                    
                                enter = input()

                            #PENGIMPLEMENTASIAN SELECTION SORTING DAN BINARY SEARCHING
                            elif pilihan_4 == "2":
                                jumlah_penjualan = [287, 391, 227, 336, 434, \
                                                    500, 135, 478, 93, 127, \
                                                    
                                                    412, 62, 354, 54, 382, \
                                                    444, 71, 312, 401, 12, \
                                                    
                                                    276, 32, 265, 11, 22, \
                                                    41, 17, 308, 418, 404]

                                sorted_penjualan_buku = selection_sorting(jumlah_penjualan)
                                while True:
                                    try:
                                        os.system('cls')
                                        WConio.textcolor(WConio.LIGHTBLUE)
                                        print("Pencarian Buku Berdasarkan Jumlah Penjualan Buku")
                                        print("================================================")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("Perhatikan Angka yang Diinput Akan Berpengaruh pada Pencarian!")
                                        WConio.textcolor(WConio.WHITE)
                                        print("")
                                        cari_penjualan_buku = int(input("Masukkan Jumlah Penjualan Buku yang Ingin Dicari = "))
                                        break
                                    except ValueError:
                                        print("")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("------------------------------")
                                        print("Input Harus Diisi dengan Angka !")
                                        print("")
                                        WConio.textcolor(WConio.YELLOW)
                                        print("Klik Enter untuk Memasukkan Input Baru yang Sesuai!")
                                        WConio.textcolor(WConio.WHITE)
                                        enter = input()
                                        os.system('cls')
                                    print("")
                                print("")

                                index, index1 = binary_searching(cari_penjualan_buku, sorted_penjualan_buku)

                                if index1 != -1:
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Buku dengan Penjualan Sebanyak =", cari_penjualan_buku, "Ditemukan!")
                                    print("")
                                    WConio.textcolor(WConio.WHITE)
                                    print("=============================")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Berikut Ini Tampilan Datanya!")
                                    print("")
                                    nama_buku = judul_buku()
                                    WConio.textcolor(WConio.WHITE)
                                    
                                    jumlah_penjualan1 = [287, 391, 227, 336, 434, \
                                                         500, 135, 478, 93, 127, \
                                                        
                                                         412, 62, 354, 54, 382, \
                                                         444, 71, 312, 401, 12, \
                                                        
                                                         276, 32, 265, 11, 22, \
                                                         41, 17, 308, 418, 404]
                        
                                    namabuku, penjualan = penjualan_buku(nama_buku, jumlah_penjualan1)

                                    print(f"{namabuku[index]} || Penjualan: {sorted_penjualan_buku[index]}")
                                    print("")

                                    with open(file_path, "w") as file:
                                        file.write("Buku dengan Penjualan Sebanyak = "+ str(cari_penjualan_buku) + " Ditemukan! \n\n")
                                        file.write("=============================\n")
                                        file.write("Berikut Ini Tampilan Datanya!\n\n")
                                        file.write(f"{namabuku[index]} || Penjualan: {sorted_penjualan_buku[index]}\n")

                                    WConio.textcolor(WConio.WHITE)
                                    print("===================================================")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Mode Pencarian Buku ! ")

                                else:
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Buku dengan Penjualan Sebanyak =", cari_penjualan_buku, "Tidak Ditemukan!")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("")
                                    print("Klik Enter untuk Kembali ke Mode Pencarian Buku ! ")
                                    
                                enter = input()

                            #PENGIMPLEMENTASIAN SELECTION SORTING DAN INTERPOLATION SEARCHING
                            elif pilihan_4 == "3":
                                tahun_buku = [2005, 1993, 1999, 2002, 2010, \
                                              1995, 2008, 2001, 1992, 2009, \
                                                    
                                              2006, 2003, 2007, 1994, 1997, \
                                              1998, 1996, 2004, 2000, 2011, \
                                                    
                                              1991, 2012, 2020, 2015, 2018, \
                                              2016, 2013, 2017, 2014, 2019]

                                sorted_tahun_buku = selection_sorting(tahun_buku)
                                                                
                                while True:
                                    try:
                                        os.system('cls')
                                        WConio.textcolor(WConio.LIGHTBLUE)
                                        print("Pencarian Buku Berdasarkan Tahun Edisi Buku")
                                        print("===========================================")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("Perhatikan Angka yang Diinput Akan Berpengaruh pada Pencarian!")
                                        WConio.textcolor(WConio.WHITE)
                                        print("")
                                        cari_tahun_buku = int(input("Masukkan Tahun Edisi Buku yang Ingin Dicari = "))
                                        break
                                    except ValueError:
                                        print("")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("------------------------------")
                                        print("Input Harus Diisi dengan Angka !")
                                        print("")
                                        WConio.textcolor(WConio.YELLOW)
                                        print("Klik Enter untuk Memasukkan Input Baru yang Sesuai!")
                                        WConio.textcolor(WConio.WHITE)
                                        enter = input()
                                        os.system('cls')
                                    print("")
                                print("")

                                index, index1 = interpolation_searching(cari_tahun_buku, sorted_tahun_buku)

                                if index1 != -1:
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Buku dengan Tahun Edisi =", cari_tahun_buku, "Ditemukan!")
                                    print("")
                                    WConio.textcolor(WConio.WHITE)
                                    print("=============================")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Berikut Ini Tampilan Datanya!")
                                    print("")
                                    nama_buku = judul_buku()
                                    WConio.textcolor(WConio.WHITE)

                                    tahun_buku = [2005, 1993, 1999, 2002, 2010, \
                                                  1995, 2008, 2001, 1992, 2009, \
                                                        
                                                  2006, 2003, 2007, 1994, 1997, \
                                                  1998, 1996, 2004, 2000, 2011, \
                                                        
                                                  1991, 2012, 2020, 2015, 2018, \
                                                  2016, 2013, 2017, 2014, 2019]
                        
                                    namabuku, tahunbuku = tahun_edisi_buku(nama_buku, tahun_buku)

                                    print(f"{namabuku[index]} || Tahun Edisi Buku: {sorted_tahun_buku[index]}")
                                    print("")

                                    with open(file_path, "w") as file:
                                        file.write("Buku dengan Tahun Edisi = "+ str(cari_tahun_buku) + " Ditemukan! \n\n")
                                        file.write("=============================\n")
                                        file.write("Berikut Ini Tampilan Datanya!\n\n")
                                        file.write(f"{namabuku[index]} || Tahun Edisi Buku: {sorted_tahun_buku[index]}\n")

                                    WConio.textcolor(WConio.WHITE)
                                    print("===================================================")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Mode Pencarian Buku ! ")

                                else:
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Buku dengan Tahun Edisi =", cari_tahun_buku, "Tidak Ditemukan!")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("")
                                    print("Klik Enter untuk Kembali ke Mode Pencarian Buku ! ")
                                    
                                enter = input()
                            
                            elif pilihan_4 == "0":
                                break
                            
                            else:
                                salahmode_anggota()
                                enter = input()
                    
                    elif pilihan_2 == "0":
                        break
                    
                    else:
                        salahmode_anggota()
                        enter = input()

            elif pilihan == "3": 
                os.system("cls")     
                menu_pinjam_buku()
                enter = input()
                os.system("cls")

                while True:
                    nama = input_nama()
                    var_nam = nama
                    nom = input_nim()
                    var_nom = nom
                    hp = input_handphone()
                    var_hp = hp

                    while True:
                        os.system("cls")
                        try:                    
                            WConio.textcolor(WConio.LIGHTRED)                
                            print("Setiap Tanggal 28/29/30/31 Perpustakaan Ini Tidak Melayani Peminjaman Buku ! ")
                            print("")
                            WConio.textcolor(WConio.WHITE)
                            tanggal, bulan, tahun = input("Tanggal/Bulan/Tahun Mulainya Peminjaman = ").split("/")

                            while (tanggal != "1" and tanggal != "2" and tanggal != "3" and tanggal != "4" and tanggal != "5" and tanggal != "6" \
                                and tanggal != "7" and tanggal != "8" and tanggal != "9" and tanggal != "10" and tanggal != "11" and tanggal != "12"\
                                and tanggal != "13" and tanggal != "14" and tanggal != "15" and tanggal != "16" and tanggal != "17" and tanggal != "18" \
                                and tanggal != "19" and tanggal != "20" and tanggal != "21" and tanggal != "22" and tanggal != "23" and tanggal != "24"\
                                and tanggal != "25" and tanggal != "26" and tanggal != "27") or \
                                (bulan != "1" and bulan != "2" and bulan != "3" and bulan != "4" and bulan != "5" and bulan != "6" and bulan != "7" \
                                and bulan != "8" and bulan != "9" and bulan != "10" and bulan != "11" and bulan != "12") or \
                                (len(tahun) != 4):
                                os.system('cls')
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Tanggal Mulainya Peminjaman Diisi Dengan Angka Semua Dengan Tanda Garis Miring [/] Sebagai Pemisah ! ")
                                print("Contoh = 12/1/2023")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Jangan Lupa Input Tanggal Hanya dari 1-27, Bulan Hanya dari 1-12, dan Tahun Harus Berjumlah 4 Digit Angka ! ")
                                print("")
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Setiap Tanggal 28/29/30/31 Perpustakaan Ini Tidak Melayani Peminjaman Buku ! ")
                                print("")
                                WConio.textcolor(WConio.WHITE)
                                tanggal,bulan,tahun = input("Tanggal/Bulan/Tahun Mulainya Peminjaman = ").split("/")

                            tang.append(tanggal)
                            bul.append(bulan)
                            tah.append(tahun)
                            var_tang = tang
                            var_bul = bul
                            var_tah = tah   
                            break

                        except ValueError:
                            print("")
                            WConio.textcolor(WConio.LIGHTRED)
                            print("----------------------------------------------------------------------------------------------------")
                            print("Tanggal Mulainya Peminjaman Diisi Dengan Angka Semua Dengan Tanda Garis Miring [/] Sebagai Pemisah ! ")
                            print("Contoh = 12/1/2023")
                            print("")
                            print("-----------------------------------------------------------------------------------------------------------")
                            print("Jangan Lupa Input Tanggal Hanya dari 1-27, Bulan Hanya dari 1-12, dan Tahun Harus Berjumlah 4 Digit Angka ! ")
                            print("")
                            WConio.textcolor(WConio.YELLOW)
                            print("Klik Enter untuk Memasukkan Tanggal Pinjam Baru yang Sesuai !")
                            WConio.textcolor(WConio.WHITE)
                            enter = input()
                        print("")
                    print("")

                    k_buku = input_kodebuku()
                    var_k_buku = k_buku   
                    var_urut_buku = k_buku

                    while True:
                        os.system("cls")
                        try:
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Setiap Tanggal 29/30/31 Perpustakaan Ini Tidak Melayani Pengembalian Buku ! ")
                            print("")
                            WConio.textcolor(WConio.WHITE)
                            tanggal_akhir, bulan_akhir, tahun_akhir = input("Tanggal/Bulan/Tahun Berakhirnya Peminjaman = ").split("/")
                            while (tanggal_akhir != "1" and tanggal_akhir != "2" and tanggal_akhir != "3" and tanggal_akhir != "4" \
                                and tanggal_akhir != "5" and tanggal_akhir != "6" and tanggal_akhir != "7" and tanggal_akhir != "8" \
                                and tanggal_akhir != "9" and tanggal_akhir != "10" and tanggal_akhir != "11" and tanggal_akhir != "12"\
                                and tanggal_akhir != "13" and tanggal_akhir != "14" and tanggal_akhir != "15" and tanggal_akhir != "16" \
                                and tanggal_akhir != "17" and tanggal_akhir != "18" and tanggal_akhir != "19" and tanggal_akhir != "20" \
                                and tanggal_akhir != "21" and tanggal_akhir != "22" and tanggal_akhir != "23" and tanggal_akhir != "24"\
                                and tanggal_akhir != "25" and tanggal_akhir != "26" and tanggal_akhir != "27" and tanggal_akhir != "28") or \
                                (bulan_akhir != "1" and bulan_akhir != "2" and bulan_akhir != "3" and bulan_akhir != "4" and bulan_akhir != "5" \
                                and bulan_akhir != "6" and bulan_akhir != "7" and bulan_akhir != "8" and bulan_akhir != "9" and bulan_akhir != "10" \
                                and bulan_akhir != "11" and bulan_akhir != "12") or \
                                (len(tahun_akhir) != 4) or (bulan_akhir != bulan) or (tahun_akhir != tahun):
                                os.system('cls')
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Tanggal Berakhirnya Peminjaman Diisi Dengan Angka Semua Dengan Tanda Garis Miring [/] Sebagai Pemisah ! ")
                                print("Contoh = 12/1/2023")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Jangan Lupa Input Tanggal Hanya dari 1-28, Bulan Hanya dari 1-12, dan Tahun Harus Berjumlah 4 Digit Angka ! ")
                                print("Ingat !, Bulan dan Tahun Berakhirnya Peminjaman Harus Sama dengan Bulan dan Tahun Mulainya Peminjaman")
                                print("")
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Setiap Tanggal 29/30/31 Perpustakaan Ini Tidak Melayani Pengembalian Buku ! ")
                                print("")
                                WConio.textcolor(WConio.WHITE)
                                tanggal_akhir, bulan_akhir, tahun_akhir = input("Tanggal/Bulan/Tahun Berakhirnya Peminjaman = ").split("/")
                            tenggat = (int(tanggal_akhir) - int(tanggal))

                            while tenggat <= 0 or tenggat > 7:
                                os.system('cls')
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Tanggal Berakhirnya Peminjaman yang Dimasukkan Kurang Tepat ! ")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Minimal 1 Hari dan Maksimal 1 Minggu Peminjaman ! ")
                                print("")  
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Setiap Tanggal 29/30/31 Perpustakaan Ini Tidak Melayani Pengembalian Buku ! ")
                                print("")        
                                WConio.textcolor(WConio.WHITE)                                                      
                                tanggal_akhir, bulan_akhir, tahun_akhir = input("Tanggal/Bulan/Tahun Berakhirnya Peminjaman = ").split("/")
                                while (tanggal_akhir != "1" and tanggal_akhir != "2" and tanggal_akhir != "3" and tanggal_akhir != "4" \
                                    and tanggal_akhir != "5" and tanggal_akhir != "6" and tanggal_akhir != "7" and tanggal_akhir != "8" \
                                    and tanggal_akhir != "9" and tanggal_akhir != "10" and tanggal_akhir != "11" and tanggal_akhir != "12"\
                                    and tanggal_akhir != "13" and tanggal_akhir != "14" and tanggal_akhir != "15" and tanggal_akhir != "16" \
                                    and tanggal_akhir != "17" and tanggal_akhir != "18" and tanggal_akhir != "19" and tanggal_akhir != "20" \
                                    and tanggal_akhir != "21" and tanggal_akhir != "22" and tanggal_akhir != "23" and tanggal_akhir != "24"\
                                    and tanggal_akhir != "25" and tanggal_akhir != "26" and tanggal_akhir != "27" and tanggal_akhir != "28") or \
                                    (bulan_akhir != "1" and bulan_akhir != "2" and bulan_akhir != "3" and bulan_akhir != "4" \
                                    and bulan_akhir != "5" and bulan_akhir != "6" and bulan_akhir != "7" and bulan_akhir != "8" \
                                    and bulan_akhir != "9" and bulan_akhir != "10" and bulan_akhir != "11" and bulan_akhir != "12") or \
                                    (len(tahun_akhir) != 4) or (bulan_akhir != bulan) or (tahun_akhir != tahun):
                                    os.system('cls')
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Tanggal Berakhirnya Peminjaman Diisi Dengan Angka Semua Dengan Tanda Garis Miring [/] Sebagai Pemisah ! ")
                                    print("Contoh = 12/1/2023")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Jangan Lupa Input Tanggal Hanya dari 1-28, Bulan Hanya dari 1-12, dan Tahun Harus Berjumlah 4 Digit Angka ! ")
                                    print("Ingat !, Bulan dan Tahun Berakhirnya Peminjaman Harus Sama dengan Bulan dan Tahun Mulainya Peminjaman")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Setiap Tanggal 29/30/31 Perpustakaan Ini Tidak Melayani Pengembalian Buku ! ")
                                    print("")
                                    WConio.textcolor(WConio.WHITE)
                                    tanggal_akhir, bulan_akhir, tahun_akhir = input("Tanggal/Bulan/Tahun Berakhirnya Peminjaman = ").split("/")   
                                tenggat = (int(tanggal_akhir) - int(tanggal))
                            teng.append(tenggat)
                            os.system("cls")
                            print("Tanggal Mulainya Peminjaman =", tanggal,"/",bulan,"/",tahun)
                            print("")
                            print("Tanggal Berakhirnya Peminjaman =", tanggal_akhir,"/",bulan_akhir,"/",tahun_akhir)
                            print("")
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Tenggat Waktu =", tenggat,"Hari")
                            print("")
                            WConio.textcolor(WConio.YELLOW)
                            print("Klik Enter untuk Lanjut ke Langkah Berikutnya ! ")
                            WConio.textcolor(WConio.WHITE)
                            enter = input()
                            tang_akh.append(tanggal_akhir)
                            bul_akh.append(bulan_akhir)
                            tah_akh.append(tahun_akhir)
                            var_tang_akh = tang_akh
                            var_bul_akh = bul_akh
                            var_tah_akh = tah_akh    
                            break
                        except ValueError:
                            print("")
                            WConio.textcolor(WConio.LIGHTRED)
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Tanggal Berakhirnya Peminjaman Diisi Dengan Angka Semua Dengan Tanda Garis Miring [/] Sebagai Pemisah ! ")
                            print("Contoh = 12/1/2023")
                            print("")
                            print("-----------------------------------------------------------------------------------------------------------")
                            print("Jangan Lupa Input Tanggal Hanya dari 1-28, Bulan Hanya dari 1-12, dan Tahun Harus Berjumlah 4 Digit Angka ! ")
                            print("")
                            WConio.textcolor(WConio.YELLOW)
                            print("Klik Enter untuk Memasukkan Tanggal Akhir Peminjaman Baru yang Sesuai !")
                            WConio.textcolor(WConio.WHITE)
                            enter = input()
                        print("")
                    print("")

                    keterangan = "Pinjam"
                    ket.append(keterangan)
                    var_ket = ket 
                    os.system("cls")
                    WConio.textcolor(WConio.LIGHTRED)
                    print("Silahkan Berikan Kartu NIM Anda ke Staff Perpustakaan Sebagai Jaminan Buku ! ")
                    print("")
                    WConio.textcolor(WConio.YELLOW)
                    print("Selamat, Peminjaman Buku Telah Berhasil Dilakukan ! ")
                    print("")

                    print("==================================================")
                    data_tambahan = ("")
                    while (data_tambahan != "YA" and data_tambahan != "TIDAK") \
                        and (data_tambahan != "Ya" and data_tambahan != "Tidak") \
                        and (data_tambahan != "ya" and data_tambahan != "tidak"):
                        WConio.textcolor(WConio.WHITE)
                        data_tambahan = input("Apakah Ingin Menambahkan Data ? (YA/TIDAK) = ")
                    i += 1
                    print("")
                    
                    if data_tambahan == "TIDAK" or data_tambahan == "Tidak" or data_tambahan == "tidak":
                        WConio.textcolor(WConio.LIGHTBLUE)
                        print("Semoga Buku yang Dipinjam Dapat Bermanfaat ! ")
                        print("")
                        WConio.textcolor(WConio.YELLOW)
                        print("Klik Enter untuk Kembali ke Halaman Utama Mode Anggota Perpustakaan ! ")
                        WConio.textcolor(WConio.WHITE)
                        enter = input()
                        break

            elif pilihan == "4":  
                os.system('cls')
                from prettytable import PrettyTable
                tabel = PrettyTable(["No", "Nama", "NIM", "No.Handphone (+62)", "Tanggal Pinjam", "Kode Buku", "Tanggal Kembali", "Keterangan"])
                if tang_akh == []:
                    WConio.textcolor(WConio.LIGHTRED)
                    print("Belum Ada yang Melakukan Aksi Peminjaman Buku !")
                    print("")
                    WConio.textcolor(WConio.YELLOW)
                    print("Klik Enter untuk Kembali ke Halaman Utama Mode Anggota Perpustakaan ! ")
                    WConio.textcolor(WConio.WHITE)
                else:
                    for a in range (i):
                        os.system("cls")
                        tabel.add_row ([a+1, var_nam[a], var_nom[a], var_hp[a], [var_tang[a], var_bul[a], var_tah[a]], var_k_buku[a], [var_tang_akh[a], var_bul_akh[a], var_tah_akh[a]], var_ket[a]])
                        print(tabel)
                        print("")
                        print("====================================================================================================================")
                        print("")
                        WConio.textcolor(WConio.YELLOW)
                        print("Data Peminjaman Buku Diatas = Valid !")
                        print("")
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Jangan Lupa untuk Mengembalikkan Buku Tepat Waktu dan")
                        print("Hubungi Pihak Staff Perpustakaan untuk Mengembalikkan Buku yang Dipinjam dan Untuk Dikembalikkan Kartu NIM yang Ditahan ! ")
                        print("")
                        WConio.textcolor(WConio.WHITE)

                        with open(file_path, "w") as file:
                            file.write(tabel.get_string() + "\n\n")
                            file.write("====================================================================================================================\n\n")
                            file.write("Data Peminjaman Buku Diatas = Valid !\n\n")
                            file.write("Jangan Lupa untuk Mengembalikkan Buku Tepat Waktu dan\n")
                            file.write("Hubungi Pihak Staff Perpustakaan untuk Mengembalikkan Buku yang Dipinjam dan Untuk Dikembalikkan Kartu NIM yang Ditahan ! \n")
                    
                    print("===================================================")
                    print("")
                    WConio.textcolor(WConio.LIGHTRED)
                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                    print("")
                    WConio.textcolor(WConio.YELLOW)
                    print("Klik Enter untuk Kembali ke Halaman Utama Mode Anggota Perpustakaan ! ")
                enter = input()

            elif pilihan == "5":  
                opsi5_anggota(tang_akh)
                enter = input()

            elif pilihan == "0":
                break
            
            else:
                salahmode_anggota()
                enter = input()

    elif pilihan_1 == "3":  
        selesai = False
        while not selesai:
            os.system("cls")
            verifikasi = menu_staff()
            os.system("cls")

            if verifikasi == "0":
                break

            elif verifikasi != "99261":
                salahkode_staff()
                enter = input()
                os.system("cls")

            elif verifikasi == "99261":
                WConio.textcolor(WConio.LIGHTGREEN)
                print("Selamat Datang di Perpustakaan Kwik Kian Gie")
                print("============================================")
                WConio.textcolor(WConio.WHITE)
                print("1. Daftar Buku yang Tersedia")
                print("2. Data Peminjaman Buku, Validasi Pengembalian Buku, dan Pemberian Denda")
                print("3. Pencarian Data Peminjaman")
                WConio.textcolor(WConio.YELLOW)

                print("0. Kembali ke Menu Utama")
                WConio.textcolor(WConio.WHITE)
                print("")

                pilihan = input("Pilih ? ") 
                os.system("cls")
                if pilihan == "1":
                    WConio.textcolor(WConio.LIGHTRED)
                    print("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! ")
                    print("")
                    urut_rating()
                    print("")

                    WConio.textcolor(WConio.LIGHTRED)
                    urut_penjualan()
                    print("")
                    
                    WConio.textcolor(WConio.LIGHTRED)
                    urut_tahun()
                    print("")

                    with open(file_path, "w") as file:
                        file.write("Untuk Setiap Buku yang Disediakan di Perpustakaan Ini Jumlahnya Infinity ! \n\n")
                        urut_rating_print(file)
                        file.write("\n")
                        urut_penjualan_print(file)
                        file.write("\n")
                        urut_tahun_print(file)

                    WConio.textcolor(WConio.WHITE)
                    print("===================================================")
                    print("")
                    WConio.textcolor(WConio.LIGHTRED)
                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                    print("")
                    WConio.textcolor(WConio.YELLOW)
                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                    WConio.textcolor(WConio.WHITE)
                    enter = input()
                    
                elif pilihan == "2": 
                    os.system('cls')
                    from prettytable import PrettyTable 
                    tabel = PrettyTable(["No", "Nama", "NIM", "No.Handphone (+62)", "Tanggal Peminjaman", "Kode Buku", "Tanggal Kembali", "Keterangan"])
                    if tang_akh == []:
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Belum Ada yang Melakukan Aksi Peminjaman Buku !")
                        print("")
                        WConio.textcolor(WConio.YELLOW)
                        print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                        WConio.textcolor(WConio.WHITE)
                        enter = input()
                    else:
                        os.system('cls')
                        for a in range (i):
                            os.system("cls")
                            tabel.add_row ([a+1, var_nam[a], var_nom[a], var_hp[a], [var_tang[a], var_bul[a], var_tah[a]], \
                                var_k_buku[a],[var_tang_akh[a], var_bul_akh[a], var_tah_akh[a]], var_ket[a]])
                            print(tabel)
                            print("")
                            print("====================================================================================================================")
                            print("")
                            WConio.textcolor(WConio.YELLOW)
                            print("Data Peminjaman Buku Diatas = Valid !")
                            print("")
                            WConio.textcolor(WConio.WHITE)

                        while True:
                            WConio.textcolor(WConio.LIGHTGREEN)
                            print("Instruksi")
                            print("=========")
                            WConio.textcolor(WConio.YELLOW)
                            print("Input Angka [0] Jika yang Dituju Tabel No. 1, Input Angka [1] Jika yang Dituju Tabel No. 2, dst ! ")
                            print("")
                            try:
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Input Angka 999 untuk Keluar dari Tampilan Ini ! ")
                                print("")
                                WConio.textcolor(WConio.WHITE)
                                pengembalian2 = int(input("Nomor Tabel Berapa yang Ingin Mengembalikkan Buku ? "))
                                if pengembalian2 == 999:
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                    WConio.textcolor(WConio.WHITE)
                                    enter = input()
                                    break
                                else:
                                    while pengembalian2 in range(len(ket)):
                                        keterangan = " Kembali"
                                        pengembalian2 = int(pengembalian2)
                                        ket[pengembalian2] = keterangan
                                        var_ket = ket

                                        print("")
                                        WConio.textcolor(WConio.LIGHTGREEN)
                                        print("==============================")
                                        WConio.textcolor(WConio.WHITE)
                                        denda = 0
                                        lama_waktu = int(input("Lama Peminjaman (Hari) : "))
                                        if lama_waktu > int((teng[pengembalian2])):
                                            denda = (lama_waktu - int(teng[pengembalian2])) * 10000
                                        print(("Harus Membayar Denda Sebesar = Rp."), denda)
                                        print("")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("Jangan Lupa Bagi Staff Perpustakaan untuk Mengembalikkan Kartu NIM yang Ditahan Bagi yang Telah Mengembalikkan Buku ! ")
                                        print("")

                                        with open(file_path, "w") as file:
                                            file.write(tabel.get_string() + "\n\n")
                                            file.write("====================================================================================================================\n\n")
                                            file.write("Data Peminjaman Buku Diatas = Valid !\n\n")
                                            file.write("Data dengan Tabel No = [" + str(pengembalian2+1) + "] dengan Lama Waktu = [" + str(lama_waktu)+ "] hari Harus Membayar Denda Sebesar = Rp." + str(denda) + "\n\n")
                                            file.write("Jangan Lupa Bagi Staff Perpustakaan untuk Mengembalikkan Kartu NIM yang Ditahan Bagi yang Telah Mengembalikkan Buku ! \n")
                                        
                                        WConio.textcolor(WConio.WHITE)
                                        print("===================================================")
                                        print("")
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                        print("")
                                        WConio.textcolor(WConio.YELLOW)
                                        print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                        WConio.textcolor(WConio.WHITE)
                                        enter = input()  
                                        break
                                    else:
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("")
                                        print("----------------------------------")
                                        print("Nomor Tabel yang Dituju Tidak Ada ! ")
                                        print("")
                                        print("Input Nomor Tabel yang Dituju Sesuai Dengan yang Telah Tersedia ! ")
                                        print("")
                                        print("Misalnya Input Angka [0] Jika yang Dituju Tabel No. 1, Input Angka [1] Jika yang Dituju Tabel No. 2, dst ! ")
                                        print("")
                                        WConio.textcolor(WConio.YELLOW)
                                        print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                        WConio.textcolor(WConio.WHITE)
                                        enter = input()

                            except ValueError:     
                                os.system('cls')
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Nomor Tabel yang Dituju Diisi Dengan Angka ! ")
                                print("")
                                print("Anda Akan Langsung Diarahkan pada Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Klik Enter untuk Melanjutkan Aksi ! ")
                                WConio.textcolor(WConio.WHITE)
                                enter = input()
                            break
                
                elif pilihan == "3":
                    WConio.textcolor(WConio.LIGHTGREEN)
                    print("Pencarian Data terkait Peminjaman Buku")
                    print("======================================")
                    WConio.textcolor(WConio.WHITE)
                    print("1. Pencarian Berdasarkan Nama Peminjam (Sequential Search)")
                    print("2. Pencarian Berdasarkan NIM Peminjam (Sequential Search)")
                    print("3. Pencarian Berdasarkan Kode Buku (Sequential Search)")
                    WConio.textcolor(WConio.YELLOW)
                    print("0. Kembali ke Menu Input Nomor Induk Staff")
                    WConio.textcolor(WConio.WHITE)
                    print("")

                    pilihan_3 = input("Pilih ? ")

                    os.system("cls")   
                    while True:
                        os.system("cls")

                        #PENGIMPLEMENTASIAN SEQUENTIAL SEARCHING
                        if pilihan_3 == "1":
                            os.system('cls')
                            WConio.textcolor(WConio.LIGHTGREEN)
                            print("Pencarian Data Berdasarkan Nama Peminjam")
                            print("========================================")
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Perhatikan Huruf Kapital & Huruf Kecil pada Awal Kata, dan Penulisan Nama Lengkap atau Tidak (Disertai dengan Spasi atau Tidak) Akan Berpengaruh pada Pencarian!")
                            WConio.textcolor(WConio.WHITE)
                            print("")
                            
                            if tang_akh == []:
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Belum Ada yang Melakukan Aksi Peminjaman Buku !")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                WConio.textcolor(WConio.WHITE)
                            
                            else:
                                cari_nama = input("Masukkan Nama yang Ingin Dicari = ")
                                index, index1 = sequential_searching(cari_nama, var_nam)

                                if index1 != -1:
                                    WConio.textcolor(WConio.WHITE)
                                    from prettytable import PrettyTable
                                    tabel1 = PrettyTable(["Nama", "NIM", "No.Handphone (+62)", "Tanggal Pinjam", "Kode Buku", "Tanggal Kembali", "Keterangan"])
                                    
                                    a = 0
                                    while a < len(index):
                                        os.system('cls')
                                        tabel1.add_row ([var_nam[index[a]], var_nom[index[a]], var_hp[index[a]], [var_tang[index[a]], var_bul[index[a]], var_tah[index[a]]], var_k_buku[index[a]], [var_tang_akh[index[a]], var_bul_akh[index[a]], var_tah_akh[index[a]]], var_ket[index[a]]])
                                        print(tabel1)
                                        a += 1
                                    print("")

                                    with open(file_path, "w") as file:
                                        file.write("Nama = "+ str(cari_nama) + " Ditemukan! \n\n")
                                        file.write("=============================\n")
                                        file.write("Berikut Ini Tampilan Datanya!\n\n")
                                        file.write(tabel1.get_string() + "\n\n")

                                    WConio.textcolor(WConio.WHITE)
                                    print("===================================================")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                else:
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Nama =", cari_nama, "Tidak Ditemukan!")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("")
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                    
                            enter = input()
                            break
                            
                        #PENGIMPLEMENTASIAN SEQUENTIAL SEARCHING
                        elif pilihan_3 == "2":
                            os.system('cls')
                            WConio.textcolor(WConio.LIGHTGREEN)
                            print("Pencarian Data Berdasarkan NIM Peminjam")
                            print("========================================")
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Perhatikan NIM yang Diinput Akan Berpengaruh pada Pencarian!")
                            WConio.textcolor(WConio.WHITE)
                            print("")
                            
                            if tang_akh == []:
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Belum Ada yang Melakukan Aksi Peminjaman Buku !")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                WConio.textcolor(WConio.WHITE)
                            
                            else:
                                cari_nim = input("Masukkan NIM yang Ingin Dicari = ")
                                index, index1 = sequential_searching(cari_nim, var_nom)

                                if index1 != -1:
                                    WConio.textcolor(WConio.WHITE)
                                    from prettytable import PrettyTable
                                    tabel2 = PrettyTable(["Nama", "NIM", "No.Handphone (+62)", "Tanggal Pinjam", "Kode Buku", "Tanggal Kembali", "Keterangan"])
                                    
                                    a = 0
                                    while a < len(index):
                                        os.system('cls')
                                        tabel2.add_row ([var_nam[index[a]], var_nom[index[a]], var_hp[index[a]], [var_tang[index[a]], var_bul[index[a]], var_tah[index[a]]], var_k_buku[index[a]], [var_tang_akh[index[a]], var_bul_akh[index[a]], var_tah_akh[index[a]]], var_ket[index[a]]])
                                        print(tabel2)
                                        a += 1
                                    print("")

                                    with open(file_path, "w") as file:
                                        file.write("NIM = "+ str(cari_nim) + " Ditemukan! \n\n")
                                        file.write("=============================\n")
                                        file.write("Berikut Ini Tampilan Datanya!\n\n")
                                        file.write(tabel2.get_string() + "\n\n")

                                    WConio.textcolor(WConio.WHITE)
                                    print("===================================================")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                else:
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("NIM =", cari_nim, "Tidak Ditemukan!")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("")
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                    
                            enter = input()
                            break

                        #PENGIMPLEMENTASIAN SEQUENTIAL SEARCHING
                        elif pilihan_3 == "3":
                            os.system('cls')
                            WConio.textcolor(WConio.LIGHTGREEN)
                            print("Pencarian Data Berdasarkan Kode Buku")
                            print("========================================")
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Perhatikan Kode Buku yang Diinput Akan Berpengaruh pada Pencarian!")
                            WConio.textcolor(WConio.WHITE)
                            print("")
                            
                            if tang_akh == []:
                                WConio.textcolor(WConio.LIGHTRED)
                                print("Belum Ada yang Melakukan Aksi Peminjaman Buku !")
                                print("")
                                WConio.textcolor(WConio.YELLOW)
                                print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                WConio.textcolor(WConio.WHITE)
                            
                            else:
                                cari_kodebuku = input("Masukkan Kode Buku yang Ingin Dicari = ")
                                index, index1 = sequential_searching(cari_kodebuku, var_k_buku)

                                if index1 != -1:
                                    WConio.textcolor(WConio.WHITE)
                                    from prettytable import PrettyTable
                                    tabel3 = PrettyTable(["Nama", "NIM", "No.Handphone (+62)", "Tanggal Pinjam", "Kode Buku", "Tanggal Kembali", "Keterangan"])
                                    
                                    a = 0
                                    while a < len(index):
                                        os.system('cls')
                                        tabel3.add_row ([var_nam[index[a]], var_nom[index[a]], var_hp[index[a]], [var_tang[index[a]], var_bul[index[a]], var_tah[index[a]]], var_k_buku[index[a]], [var_tang_akh[index[a]], var_bul_akh[index[a]], var_tah_akh[index[a]]], var_ket[index[a]]])
                                        print(tabel3)
                                        a += 1
                                    print("")

                                    with open(file_path, "w") as file:
                                        file.write("Kode Buku = "+ str(cari_kodebuku) + " Ditemukan! \n\n")
                                        file.write("=============================\n")
                                        file.write("Berikut Ini Tampilan Datanya!\n\n")
                                        file.write(tabel3.get_string() + "\n\n")

                                    WConio.textcolor(WConio.WHITE)
                                    print("===================================================")
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Hasil Output juga Ditampilkan pada File .txt ! ")
                                    print("")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                else:
                                    print("")
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Kode Buku =", cari_kodebuku, "Tidak Ditemukan!")
                                    WConio.textcolor(WConio.YELLOW)
                                    print("")
                                    print("Klik Enter untuk Kembali ke Input Nomor Induk Staff untuk Keamanan Mode Ini ! ")
                                    
                            enter = input()
                            break
                        
                        elif pilihan_3 == "0":
                            break
                        
                        else:
                            salahmode_anggota()
                            enter = input()
                            break

                elif pilihan == "0":
                    break
                
                else:
                    salahmode_staff()
                    enter = input()

    elif pilihan_1 == "0":
        WConio.textcolor(WConio.YELLOW)
        print("Terima Kasih Telah Menggunakan Library's Helper Application ! ")
        print("")
        WConio.textcolor(WConio.WHITE)
        selesai = True
    
    else:
        salahmode_menuutama()
        enter = input()