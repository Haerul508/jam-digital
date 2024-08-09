import tkinter as tk
import time

# Membuat jendela utama
root = tk.Tk()
root.title("Jam Digital")

# Membuat label untuk menampilkan waktu
label_waktu = tk.Label(root, font=("Arial", 50), bg="black", fg="white")
label_waktu.pack(anchor='center')

# Fungsi untuk memperbarui waktu setiap detik
def perbarui_waktu():
    waktu_sekarang = time.strftime("%H:%M:%S")
    label_waktu.config(text=waktu_sekarang)
    label_waktu.after(1000, perbarui_waktu)

# Memulai pembaruan waktu
perbarui_waktu()

# Menjalankan aplikasi
root.mainloop()
