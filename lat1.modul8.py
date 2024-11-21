def penjumlahan_rekursif(n, current=1, total=0):
    if current > n:
        return total
    else:
        angka = int(input(f"Masukkan angka ke-{current}: "))
        return penjumlahan_rekursif(n, current + 1, total + angka)

def jalankan_penjumlahan():
    jumlah = int(input("Masukkan Jumlah: "))
    hasil = penjumlahan_rekursif(jumlah)
    print(f"Hasil penjumlahan adalah: {hasil}")

jalankan_penjumlahan()
