def pangkat(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * pangkat(x, y - 1)
    else:
        return 1 / pangkat(x, -y)

while True:
    x_input = input("Masukkan nilai angka (x) (tekan Enter untuk berhenti): ")
    if x_input == "":
        break
    y_input = input("Masukkan nilai pangkat (y): ")
    if y_input == "":
        break

    try:
        x = int(x_input)
        y = int(y_input)
        hasil = pangkat(x, y)
        print(f"{x} dipangkatkan {y} = {hasil}")
    except ValueError:
        print("Input harus berupa angka. Coba lagi.")
