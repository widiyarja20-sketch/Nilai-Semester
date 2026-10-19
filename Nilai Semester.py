print("=== Aplikasi Hitung Nilai Semester ===")

try:
    # Input nilai dari user
    tugas = float(input("Masukkan nilai Tugas (20%): "))
    uts = float(input("Masukkan nilai UTS (30%): "))
    uas = float(input("Masukkan nilai UAS (50%): "))

    # Hitung nilai akhir berdasarkan bobot
    nilai_akhir = (tugas * 0.2) + (uts * 0.3) + (uas * 0.5)

    # Tentukan grade nilai
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D/E"

    print("\n--- Hasil ---")
    print(f"Nilai Akhir: {nilai_akhir:.2f}") # Membatasi 2 angka di belakang koma
    print(f"Grade: {grade}")

except ValueError:
    print("\nError: Mohon masukkan angka yang valid!")
