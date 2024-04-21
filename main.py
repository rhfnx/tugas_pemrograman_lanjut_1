def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
  nilai_akhir = 0.25 * nilai_tugas + 0.35 * nilai_uts + 0.4 * nilai_uas

  if nilai_akhir > 85:
    predikat = "A"
  elif nilai_akhir > 80:
    predikat = "A-"
  elif nilai_akhir > 75:
    predikat = "B+"
  elif nilai_akhir > 70:
    predikat = "B"
  elif nilai_akhir > 65:
    predikat = "B-"
  elif nilai_akhir > 60:
    predikat = "C+"
  elif nilai_akhir > 55:
    predikat = "C"
  elif nilai_akhir > 50:
    predikat = "C-"
  elif nilai_akhir > 30:
    predikat = "D"
  else:
    predikat = "E"

  return nilai_akhir, predikat

def main():
  nama = input("Masukkan nama mahasiswa: ")
  nilai_tugas = float(input("Masukkan nilai tugas: "))
  nilai_uts = float(input("Masukkan nilai UTS: "))
  nilai_uas = float(input("Masukkan nilai UAS: "))

  nilai_akhir, predikat = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

  print(f"Nama: {nama}")
  print(f"Nilai Tugas: {nilai_tugas}")
  print(f"Nilai UTS: {nilai_uts}")
  print(f"Nilai UAS: {nilai_uas}")
  print(f"Nilai Akhir: {nilai_akhir:.2f}")
  print(f"Predikat: {predikat}")

if __name__ == "__main__":
  main()
