# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tC2K3QTFw-_8sJiXCFoT4OpLy4m5RyQJ
"""

# Gerekli kütüphaneyi içe aktar
import socket

# Hedef IP adresini tanımlıyoruz
target_ip = "127.0.0.1"  # kendi bilgisayarımız (localhost)

# Hedef portu tanımlıyoruz
target_port = 80  # HTTP portu

# Bir soket (bağlantı kanalı) oluşturuyoruz
# AF_INET = IPv4, SOCK_STREAM = TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Zaman aşımı koyuyoruz (bağlantı süresi uzun olmasın diye)
sock.settimeout(2)

# Bağlanmayı deniyoruz
result = sock.connect_ex((target_ip, target_port))

# Eğer sonuç 0 ise port açıktır
if result == 0:
    print(f"Port {target_port} açık!")
else:
    print(f"Port {target_port} kapalı.")

# Soketi kapatıyoruz
sock.close()

# Gerekli kütüphaneyi ekliyoruz
import socket

# IP adresini kullanıcıdan alıyoruz
target_ip = input("Tarama yapılacak IP adresini girin (örneğin 127.0.0.1): ")

# Başlangıç ve bitiş portlarını alıyoruz
start_port = int(input("Başlangıç portu: "))
end_port = int(input("Bitiş portu: "))

print(f"\n{target_ip} adresinde {start_port}-{end_port} arası portlar taranıyor...\n")

# Belirtilen port aralığında döngü ile geziyoruz
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Bağlantı süresi sınırı
    result = sock.connect_ex((target_ip, port))  # Port açık mı test et

    if result == 0:
        print(f"Port {port} açık.")
    else:
        print(f"Port {port} kapalı.")

    sock.close()

