from view.view_nilai import *
print("Nama : Rico Prasetya")
print("NIM  : 312210425")
print("")
print("-----Program Sederhana Python-----")
print("")
while True:
    print("-------Fitur yang tersedia--------")
    print("=>Tambah data =>Ketik T")
    print("=>Ubah data   =>Ketik U")
    print("=>Hapus data  =>Ketik H")
    print("=>Cari data   =>Ketik C")
    print("=>Cetak data  =>Ketik P")
    print("=>Exit        =>Ketik E")
    print("----------------------------------")
    print("")
    perintah=input("Ketikkan Perintah => ")
    print("")
    if (perintah == "t"):
        tambah_data()
    elif (perintah == "u"):
        ubah_data()
    elif (perintah == "h"):
        hapus_data()
    elif (perintah == "c"):
        cetak_hasil_pencarian()
    elif (perintah == "p"):
        cetak_daftar_nilai()
    elif (perintah == "e"):
        print("--Terima kasih telah menggunakan program ini--")
        print("")
        break
    else:
        print("--Perintah yang anda masukkan salah--")
        print("")
