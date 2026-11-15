import tkinter as tk
from tkinter import messagebox


# Membuat objek 
app = ()

# jendela 
window = tk.Tk()
window.title("Aplikasi Tanpa AI")
window.geometry("400x300")
window.configure(bg="lightblue")

#judul 
judul = tk.Label(
    window,
    text = "Selamat Datang di Aplikasi Tanpa AI",  
    font = ("Arial", 16, "bold"),
    bg = "lightblue" 
)
judul.pack(pady=20)


# button
tk.Button(
    window,
    text = "Klik Saya",
    font = ("Arial", 14),
).pack(pady=10)

# kuncinya disini ketika ingin menampilkan hasilnya 
window.mainloop()

