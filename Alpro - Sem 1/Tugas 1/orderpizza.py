print('\nSelamat datang di Pizza Hut')
print('\nSilahkan pilih menu topping pizza anda :')
print('- Frankfurter')
print('- Meat Monsta')
print('- Super Supreme')
print('- Super Supreme Chicken')

topping = str(input('Masukkan menu pilihan anda: '))

if topping == 'Frankfurter':
    harga_topping = 40000
    
elif topping == 'Meat Monsta':
    harga_topping = 45000
    
elif topping == 'Super Supreme':
    harga_topping = 50000
    
elif topping == 'Super Supreme Chicken':
    harga_topping = 55000
else :
    print("Pilihan Anda tidak valid. Silahkan ulangi program.")

print("Silahkan pilih crust pizza Anda: ")
print("- Pan Pizza")
print("- CheesyBites")
print("- Crowncrust")
print("- StuffedCrust")

crust = str(input("Masukkan pilihan crust pizza Anda: "))

if crust in ['Pan Pizza', 'CheesyBites', 'Crowncrust', 'StuffedCrust']:
    harga_crust = 12000
else: print("Pilihan Anda tidak valid. Silahkan ulangi program.")

print("Silahkan pilih ukuran pizza Anda: ")
print("- Personal")
print("- Medium")
print("- Large") 

Ukuran = str(input("Masukkan pilihan Ukuran pizza Anda: "))

if Ukuran == "Personal":
 harga_ukuran = 10000
elif Ukuran == "Medium":
  harga_ukuran = 15000
elif Ukuran == "Large":
  harga_ukuran = 20000
else: print("Ukuran yang anda masukkan tidak valid.")

tambah_keju = input("\nApakah Anda ingin menambah ekstra keju? (y/n)")
if tambah_keju == 'y' :
    harga_keju = 13000
    print("Dengan tambahan keju")
    elif tambah_keju == 'n' :
    harga_keju = 0
    print("Tanpa tambahan keju")
else :
    print("Jawaban Anda tidak valid")

total_harga = harga_topping + harga_crust + harga_ukuran + harga_keju

print("Thank you for choosing Pizza Hut Deliveries!")
print("Your final bill is: Rp", total_harga)
