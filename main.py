catatan = []


def tambah_catatan():
    """Minta input mapel, topik, durasi (menit) lalu simpan ke list catatan."""
    mapel = input("Masukkan nama mapel: ").strip()
    topik = input("Masukkan topik: ").strip()

    while True:
        durasi_str = input("Masukkan durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_str)
            if durasi <= 0:
                print("Durasi harus lebih dari 0. Coba lagi.")
                continue
            break
        except ValueError:
            print("Masukkan angka bulat untuk durasi. Coba lagi.")

    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    catatan.append(catatan_baru)
    print("\nCatatan berhasil ditambahkan!\n")


def lihat_catatan():
    """Tampilkan semua catatan yang tersimpan dalam tabel rapi.

    Jika belum ada catatan, tampilkan pesan yang sesuai.
    """
    if not catatan:
        print("Belum ada catatan.\n")
        return

    # Hitung lebar kolom berdasarkan konten agar rata
    no_w = len(str(len(catatan)))
    mapel_w = max(len("Mapel"), max((len(c["mapel"]) for c in catatan), default=0))
    topik_w = max(len("Topik"), max((len(c["topik"]) for c in catatan), default=0))
    durasi_w = len("Durasi (menit)")

    # Header
    print("\n=== Daftar Catatan Belajar ===")
    header = f"{'No'.ljust(no_w)}  {'Mapel'.ljust(mapel_w)}  {'Topik'.ljust(topik_w)}  {'Durasi (menit)'.rjust(durasi_w)}"
    print(header)
    print('-' * len(header))

    # Baris data
    for i, c in enumerate(catatan, 1):
        no = str(i).ljust(no_w)
        mapel = c['mapel'].ljust(mapel_w)
        topik = c['topik'].ljust(topik_w)
        durasi = str(c.get('durasi', 0)).rjust(durasi_w)
        print(f"{no}  {mapel}  {topik}  {durasi}")
    print()


def total_waktu():
    """Hitung dan tampilkan total waktu belajar dari semua catatan."""
    if not catatan:
        print("Belum ada catatan.\n")
        return

    total = sum(c.get('durasi', 0) for c in catatan)
    print(f"\nTotal waktu belajar: {total} menit\n")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")