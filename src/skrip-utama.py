from luas.segitiga import hitung_luas as hls
from luas.persegi import hitung_luas as hlp
from luas.lingkaran import hitung_luas as hll
from volume.bola import hitung_volume as hvb
from volume.kubus import hitung_volume as hvk
from volume.prisma import hitung_volume as hvp

#Luas Segitiga
print("\n~ Menghitung Luas Segitiga")
print("Alas = " ,(21))
print("Tinggi = " ,(4))
print("Luas Segitiga = " ,hls(21,4))

#Luas Lingkaran 
print("\n~ Menghitung luas Lingkaran")
print("Radius = " ,(14))
print("Luas Lingkaran = " ,hll(14))

#Luas Persegi
print("\n~ Menghitung Luas Persegi")
print("Sisi = " ,(23))
print("Luas Persegi = " ,hlp(23))

#Volume Kubik
print("\n~ Menghitung Volume Kubus")
print("Sisi = " ,(20))
print("Volume Kubus = " ,hvk(20))

#Volume Bola
print("\n~ Menghitung Volume Bola")
print("Radius = " ,(43))
print("Volume Bola = " ,hvb(43))

#Volume Prisma
print("\n~ Menghitung Volume Prisma")
print("Als = " ,(6))
print("Ts = " ,(9))
print("Tp = " ,(7))
print("Volume Prisma = ",hvp(6,9,7))