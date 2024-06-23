import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import mplcursors  # Import modułu mplcursors

# Autor: Zolwik Krystian Staśkiewicz

# Pobranie ścieżki do katalogu programu
program_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(program_directory, 'dane_wykresu.txt')

def wczytaj_dane_z_pliku():
    try:
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines[:30]):
            data = line.strip().split(':')
            if len(data) == 2:
                data_entry = data[0].strip()
                value_entry = data[1].strip()
                entry_daty[i].delete(0, tk.END)
                entry_daty[i].insert(0, data_entry)
                entry_wartosci[i].delete(0, tk.END)
                entry_wartosci[i].insert(0, value_entry)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się wczytać danych z pliku: {e}")

def zapisz_wykres(format):
    try:
        # Pobieranie danych z tabeli
        wartosci = []
        daty = []
        for i in range(30):
            wartosc = entry_wartosci[i].get()
            data = entry_daty[i].get()
            if wartosc and data:  # Sprawdzanie czy pole nie jest puste
                wartosci.append(float(wartosc))
                daty.append(data)
        
        # Zapisywanie danych do pliku
        with open(file_path, 'w') as file:
            for wartosc, data in zip(wartosci, daty):
                file.write(f'{data}: {wartosc}\n')
        
        # Tworzenie wykresu
        plt.figure(figsize=(10, 6))
        
        # Regresja liniowa
        x = np.arange(len(wartosci)).reshape(-1, 1)
        model = LinearRegression()
        model.fit(x, wartosci)
        y_pred = model.predict(x)
        plt.plot(daty, y_pred, color='r', linestyle='--', linewidth=2, label='Regresja liniowa')
        
        plt.plot(daty, wartosci, marker='o', color='b', linestyle='-', linewidth=2, label='Wartość')
        plt.xlabel('Data')
        plt.ylabel('Wartość')
        plt.title(entry_tytul.get())
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Pobranie bieżącej daty i godziny
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Utworzenie nazwy pliku z datą i godziną
        filename = f'wykres_{current_datetime}.{format}'
        filepath = os.path.join(program_directory, filename)
        
        # Zapisywanie wykresu do pliku w wybranym formacie
        plt.savefig(filepath)
        
        # Wyświetlanie komunikatu o pomyślnym zapisaniu
        messagebox.showinfo("Sukces", f"Wykres został pomyślnie zapisany jako '{filename}'")
        
        # Analiza danych
        srednia = np.mean(wartosci)
        maksimum = np.max(wartosci)
        minimum = np.min(wartosci)
        odchylenie_std = np.std(wartosci)
        
        analiza = f"Średnia: {srednia}\n" \
                  f"Maksimum: {maksimum}\n" \
                  f"Minimum: {minimum}\n" \
                  f"Odchylenie: {odchylenie_std}"
        
        # Dodanie tekstu z analizą na wykresie
        plt.text(0.02, 0.98, analiza, transform=plt.gca().transAxes,
                 verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
        
        # Dodanie interaktywnych etykiet dla punktów danych
        cursor = mplcursors.cursor(hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(
            f'Wartość: {sel.target[1]:.2f}\nData: {daty[int(sel.target[0])]}'))
        
        # Wyświetlenie wykresu
        plt.show()
        
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania wykresu: {e}")

# Tworzenie interfejsu użytkownika
root = tk.Tk()
root.title("Generowanie wykresu z wczytanymi danymi")

# Przycisk do wczytania danych z pliku
button_wczytaj = ttk.Button(root, text="Wczytaj dane z pliku", command=wczytaj_dane_z_pliku)
button_wczytaj.grid(row=0, column=0, columnspan=4)

# Tworzenie tabeli do wprowadzania danych
entry_wartosci = []
entry_daty = []
for i in range(30):
    label_wartosc = ttk.Label(root, text="Wartość:")
    label_wartosc.grid(row=i+1, column=0)
    entry_wartosc = ttk.Entry(root)
    entry_wartosc.grid(row=i+1, column=1)
    entry_wartosci.append(entry_wartosc)
    
    label_data = ttk.Label(root, text="Data:")
    label_data.grid(row=i+1, column=2)
    entry_data = ttk.Entry(root)
    entry_data.grid(row=i+1, column=3)
    entry_daty.append(entry_data)

# Pole do wprowadzenia tytułu
label_tytul = ttk.Label(root, text="Tytuł wykresu:")
label_tytul.grid(row=31, column=0)
entry_tytul = ttk.Entry(root)
entry_tytul.grid(row=31, column=1, columnspan=3)

# Pole wyboru formatu zapisu
label_format = ttk.Label(root, text="Format zapisu:")
label_format.grid(row=32, column=0)
format_var = tk.StringVar()
format_var.set("png")  # Domyślny format to PNG
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=["png", "pdf", "svg"])
format_dropdown.grid(row=32, column=1)

def generuj_wykres_i_zapisz():
    format = format_var.get()
    zapisz_wykres(format)

# Przycisk do generowania wykresu i zapisywania danych
button = ttk.Button(root, text="Generuj wykres i zapisz dane", command=generuj_wykres_i_zapisz)
button.grid(row=33, column=0, columnspan=4)

# Pasek stanu na dole okna
status_bar = tk.Label(root, text="Autor: zolwikC Krystian Staśkiewicz", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.grid(row=34, column=0, columnspan=4, sticky=tk.W+tk.E)

root.mainloop()
