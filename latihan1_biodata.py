def tampilkan_biodata():
    # Data biodata yang diset langsung
    nama = "I Putu Andra Septa Raditya"
    nim = "2601010038"
    prodi = "Sistem Informasi"
    fakultas = "FTID"
    hobi = "Robotik (Sumobot)"

    # Menampilkan kartu biodata
    print("=" * 45)
    print("            KARTU BIODATA ANDA")
    print("=" * 45)
    print(f" Nama Lengkap   : {nama}")
    print(f" NIM / NPM      : {nim}")
    print(f" Program Studi  : {prodi}")
    print(f" Fakultas       : {fakultas}")
    print(f" Hobi           : {hobi}")
    print("=" * 45)


if __name__ == "__main__":
    tampilkan_biodata()