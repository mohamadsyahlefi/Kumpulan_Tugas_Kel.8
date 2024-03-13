class MenuItem:
    def __init__(self, NamaMenu, Harga):
        self.NamaMenu = NamaMenu
        self.Harga = Harga
        self.next = None

head = None
tail = None
current = None

def addMenuItem(NamaMenu, Harga):
    global head, tail, current
    newItem = MenuItem(NamaMenu, Harga)
    newItem.next = None
    
    if head == None:
        head = newItem
        tail = newItem
        current = newItem
    else:
        tail.next = newItem
        tail = newItem

def DisplayMenu():
     current = head
     while current != None:
         print(current.NamaMenu, "Rp.", current.Harga)
         current = current.next

print("\n~~~~~~~~~~~~~~~~~~~~")
print("Selamat Datang di Warung D4 MIE")
print("~~~~~~~~~~~~~~~~~~~~")

print("\nDaftar Menu:")
addMenuItem("Mixue Ice Cream", 5000)
addMenuItem("Boba Shake", 16000)
addMenuItem("Mi Sundae", 14000)
addMenuItem("Mie Ganas", 11000)
addMenuItem("Creamy Mango Boba", 22000)
DisplayMenu()

totalHarga = 0
pesanan = []
harga = []
Jml_Pesanan = 0

while True:
     order = input("\nSilahkan ketik pesanan Anda: ")
    
     if order == "selesai":
         break
     print(f"\n{order} sudah ditambahkan ke keranjang")
     print("-----------------------------------")
    
# // BAGIAN DITRYA
#     current = head
#     while current != None:
#         if current.NamaMenu == order:
#             pesanan.append(current.NamaMenu)
#             harga.append(current.Harga)
#             Jml_Pesanan += 1
#             totalHarga += current.Harga
#             break
#         current = current.next
    
#     print("\n|| Pesanan Anda ||")
#     for i in range(Jml_Pesanan):
#         print(pesanan[i], "Rp.", harga[i])
#     print("\n-----------------------------------")
#     print("(Ketik 'selesai' untuk step berikutnya) ")
#     print("-----------------------------------")
    
# print("\nTotal harga pesanan Anda: Rp.", totalHarga)
# print("-----------------------------------")

# print("\n------Terima Kasih telah memesan di Warung Kami------\n")
