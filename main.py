# To-Do List Sederhana
FILENAME = "todolist.txt"

def baca_tugas():
    try:
        with open(FILENAME, "r") as file:
            return [baris.strip() for baris in file.readlines()]
    except FileNotFoundError:
        return []

def simpan_tugas(tugas):
    with open(FILENAME, "w") as file:
        for item in tugas:
            file.write(item + "\n")

def tampilkan_tugas(tugas):
    if not tugas:
        print("Belum ada tugas.")
    else:
        print("\n--- Daftar Tugas ---")
        for i, item in enumerate(tugas, start=1):
            print(f"{i}. {item}")

def tambah_tugas(tugas):
    item = input("Masukkan tugas baru: ").strip()
    if item:
        tugas.append(item)
        simpan_tugas(tugas)
        print("Tugas berhasil ditambahkan.")
    else:
        print("Tugas tidak boleh kosong!")

def hapus_tugas(tugas):
    tampilkan_tugas(tugas)
    try:
        idx = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= idx < len(tugas):
            removed = tugas.pop(idx)
            simpan_tugas(tugas)
            print(f"Tugas '{removed}' berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang benar!")

def menu():
    tugas = baca_tugas()
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Tampilkan Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tampilkan_tugas(tugas)
        elif pilihan == "2":
            tambah_tugas(tugas)
        elif pilihan == "3":
            hapus_tugas(tugas)
        elif pilihan == "4":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
