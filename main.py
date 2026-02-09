import sys

catatan = []
favorit_mapel = set()


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
    print("i\nCatatan berhasil ditambahkan!\n")


def lihat_catatan():
    """Tampilkan semua catatan yang tersimpan dalam tabel rapi.

    Jika belum ada catatan, tampilkan pesan yang sesuai.
    """
    

    tampilkan_catatan(catatan)


def tampilkan_catatan(list_cat):
    """Tampilkan daftar catatan dari `list_cat` dengan format tabel.

    Fungsi ini digunakan ulang oleh fungsi lain (filter).
    """
    if not list_cat:
        print("\nBelum ada catatan untuk ditampilkan.\n")
        input("Tekan Enter untuk kembali ke menu...")
        return

    # Hitung lebar kolom berdasarkan konten agar rata
    no_w = len(str(len(list_cat)))
    mapel_w = max(len("Mapel"), max((len(c["mapel"]) for c in list_cat), default=0))
    topik_w = max(len("Topik"), max((len(c["topik"]) for c in list_cat), default=0))
    durasi_w = len("Durasi (menit)")

    # Header
    print("\n=== Daftar Catatan Belajar ===")
    header = f"{ 'No'.ljust(no_w)}  { 'Mapel'.ljust(mapel_w)}  { 'Topik'.ljust(topik_w)}  { 'Durasi (menit)'.rjust(durasi_w)}"
    print(header)
    print('-' * len(header))

    # Baris data
    for i, c in enumerate(list_cat, 1):
        no = str(i).ljust(no_w)
        mapel = c['mapel'].ljust(mapel_w)
        topik = c['topik'].ljust(topik_w)
        durasi = str(c.get('durasi', 0)).rjust(durasi_w)
        mark = ' *' if c['mapel'] in favorit_mapel else ''
        print(f"{no}  {mapel}  {topik}  {durasi}{mark}")
    print()
    input("Tekan Enter untuk kembali ke menu...")


def toggle_favorit():
    """Tandai atau hapus tanda mapel sebagai favorit."""
    if not catatan:
        print("\nBelum ada catatan yang bisa diberi favorit. Tambahkan catatan dulu.\n")
        input("Tekan Enter untuk kembali ke menu...")
        return

    # Tampilkan daftar mapel unik
    mapel_unik = sorted({c['mapel'] for c in catatan})
    print("\nMapel yang tersedia:")
    for i, m in enumerate(mapel_unik, 1):
        status = "(favorit)" if m in favorit_mapel else ""
        print(f"{i}. {m} {status}")

    nama = input("Masukkan nama mapel yang ingin ditandai/dihapus favorit: ").strip()
    if not nama:
        print("Tidak ada mapel yang dipilih.")
        return

    # Cari nama mapel dengan perbandingan case-insensitive
    matches = [m for m in mapel_unik if m.lower() == nama.lower()]
    if not matches:
        print("Mapel tidak ditemukan di catatan.")
        input("Tekan Enter untuk kembali ke menu...")
        return

    target = matches[0]
    if target in favorit_mapel:
        favorit_mapel.remove(target)
        print(f"Mapel '{target}' dihapus dari favorit.")
    else:
        favorit_mapel.add(target)
        print(f"Mapel '{target}' ditambahkan ke favorit.")

    input("Tekan Enter untuk kembali ke menu...")


def filter_per_mapel():
    """Tampilkan catatan yang hanya untuk mapel tertentu."""
    if not catatan:
        print("\nBelum ada catatan untuk difilter.\n")
        input("Tekan Enter untuk kembali ke menu...")
        return

    mapel_unik = sorted({c['mapel'] for c in catatan})
    print("\nPilih mapel untuk menampilkan catatan:")
    for i, m in enumerate(mapel_unik, 1):
        status = "(favorit)" if m in favorit_mapel else ""
        print(f"{i}. {m} {status}")

    pilihan = input("Masukkan nomor mapel atau ketik nama mapel: ").strip()
    if not pilihan:
        print("Tidak ada pilihan.")
        return

    # Coba nomor
    target_mapel = None
    if pilihan.isdigit():
        idx = int(pilihan) - 1
        if 0 <= idx < len(mapel_unik):
            target_mapel = mapel_unik[idx]
    else:
        matches = [m for m in mapel_unik if m.lower() == pilihan.lower()]
        if matches:
            target_mapel = matches[0]

    if not target_mapel:
        print("Mapel tidak ditemukan.")
        input("Tekan Enter untuk kembali ke menu...")
        return

    filtered = [c for c in catatan if c['mapel'].lower() == target_mapel.lower()]
    tampilkan_catatan(filtered)


def total_waktu():
    """Hitung dan tampilkan total waktu belajar dari semua catatan."""
    

    total = sum(c.get('durasi', 0) for c in catatan)
    print(f"\nTotal waktu belajar: {total} menit\n")
    pilihan = input("Tekan Enter untuk kembali ke menu atau ketik 'q' untuk keluar: ").strip().lower()
    if pilihan == 'q':
        print("Terima kasih, terus semangat belajar!")
        sys.exit(0)

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Tandai / hapus Mapel favorit")
    print("6. Lihat catatan per mapel (filter)")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "5":
        toggle_favorit()
    elif pilihan == "6":
        filter_per_mapel()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")