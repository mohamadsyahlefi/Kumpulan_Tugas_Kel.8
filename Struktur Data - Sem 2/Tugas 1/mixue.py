class Node:
    def __init__(self, item, harga):
        self.harga = harga
        self.item = item
        self.next = None

class Menu:
    def __init__(self, item, harga):
        new_node = Node(item, harga)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, item, harga):
        new_node = Node(item, harga)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def display_item(self):
        temp = self.head
        nomor_item = 1

        print("\nDaftar Menu:")
        while temp:
            print(f"{nomor_item}. {temp.item}, {temp.harga} rupiah")
            temp = temp.next
            nomor_item += 1
    
    def display_pesanan(self):
        temp = self.head  # Mulai dari node setelah head karena head adalah menu default
        nomor_item = 1
        while temp:
            temp = temp.next
            nomor_item += 1
            print(f"{nomor_item}. {temp.item}, Rp.{temp.harga}")
    # def display_pesanan(self):
    #     temp = self.head
    #     nomor_item = 1
    #     print("\nPesanan anda")
    #     while temp:
            # if temp.item != "Miexue ice cream":
            #     print(f"{nomor_item}. {temp.item}, {temp.harga} ")
            #     nomor_item += 1
            #     temp = temp.next

    def total_harga(self):
        total = 0
        total_harga = self.head
        while total_harga:
            total += total_harga.harga
            total_harga = total_harga.next
        return total
    
    def find_harga(self, item):
        temp = self.head
        while temp:
            if temp.item() == item():
                return temp.harga
            temp = temp.next
        return None

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Selamat Datang di Warung D4 MIE")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

miexue_menu = Menu("Miexue ice cream", 5000)
miexue_menu.append("Boba shake", 16000)
miexue_menu.append("Mi sundae", 14000)
miexue_menu.append("Mi ganas", 11000)
miexue_menu.append("Creamy mango boba", 22000)
miexue_menu.display_item()

while True:
    print("\n1. Pesan Menu Miexue")
    print("2. Tampikan Pesanan Saya")
    print("3. Bayar Pesanan")
    choice = input("Pilih opsi (1/2/3): ")

    if choice == "1":
        item = input("Masukkan Pilihan Menu: ")
        harga_item = miexue_menu.find_harga(item)
        if harga_item is not None:
            miexue_menu.append(item, harga_item)
            print(f"\n{item} sudah ditambahkan ke keranjang")
        else:
            print(f"Menu '{item}' tidak ditemukan.")
        
    # elif choice == "2":
    #     print("\nPesanan Anda:")
    #     miexue_menu.display_pesanan()
    # elif choice == "3":
    #     total_pesanan = miexue_menu.total_harga()
    #     print(f"Total biaya yang harus dibayarkan adalah {total_pesanan} rupiah.\nTerimakasih sudah memesan")