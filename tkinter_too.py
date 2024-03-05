import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import csv
from PIL import Image, ImageTk
import os
import shutil

class LemmikloomadeVarjupaik:
    def __init__(self, root):
        self.root = root
        self.root.title("Lemmikloomade Varjupaik")

        # Lemmikloomade andmete struktuur: ID, Nimi, Liik, Vanus, Sugu, Pilt
        self.lemmikloomad = []

        # Säilitame PhotoImage instantsid, et need ei häviks
        self.photo_images = []

        # GUI elemendid
        self.label_nimi = tk.Label(root, text="Nimi:")
        self.label_liik = tk.Label(root, text="Liik:")
        self.label_vanus = tk.Label(root, text="Vanus:")
        self.label_sugu = tk.Label(root, text="Sugu:")
        self.label_pilt = tk.Label(root, text="Pilt (failinimi):")

        self.entry_nimi = tk.Entry(root)
        self.entry_liik = tk.Entry(root)
        self.entry_vanus = tk.Entry(root)
        self.entry_sugu = tk.Entry(root)
        self.entry_pilt = tk.Entry(root)

        self.button_lisa = tk.Button(root, text="Lisa Lemmikloom", command=self.lisa_lemmikloom)
        self.button_kuva = tk.Button(root, text="Kuva Lemmikloomad", command=self.kuva_lemmikloomad)
        self.button_salvesta = tk.Button(root, text="Salvesta", command=self.salvesta_andmed)
        self.button_kustuta = tk.Button(root, text="Kustuta Lemmikloom", command=self.kustuta_lemmikloom)
        self.button_lisa_pilt = tk.Button(root, text="Lisa/Uuenda Pilt", command=self.lisa_uuenda_pilt)

        # Paigutus
        self.label_nimi.grid(row=0, column=0)
        self.label_liik.grid(row=1, column=0)
        self.label_vanus.grid(row=2, column=0)
        self.label_sugu.grid(row=3, column=0)
        self.label_pilt.grid(row=4, column=0)

        self.entry_nimi.grid(row=0, column=1)
        self.entry_liik.grid(row=1, column=1)
        self.entry_vanus.grid(row=2, column=1)
        self.entry_sugu.grid(row=3, column=1)
        self.entry_pilt.grid(row=4, column=1)

        self.button_lisa.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_kuva.grid(row=6, column=0, columnspan=2, pady=10)
        self.button_salvesta.grid(row=7, column=0, columnspan=2, pady=10)
        self.button_kustuta.grid(row=8, column=0, columnspan=2, pady=10)
        self.button_lisa_pilt.grid(row=9, column=0, columnspan=2, pady=10)

    def lisa_lemmikloom(self):
        nimi = self.entry_nimi.get()
        liik = self.entry_liik.get()
        vanus = self.entry_vanus.get()
        sugu = self.entry_sugu.get()
        pilt = self.entry_pilt.get()

        # Genereeri unikaalne ID
        lemmiklooma_id = len(self.lemmikloomad) + 1

        # Lisa lemmiklooma andmed listi
        lemmiklooma_andmed = [lemmiklooma_id, nimi, liik, vanus, sugu, pilt]
        self.lemmikloomad.append(lemmiklooma_andmed)

        # Tühjenda sisestusväljad
        self.entry_nimi.delete(0, tk.END)
        self.entry_liik.delete(0, tk.END)
        self.entry_vanus.delete(0, tk.END)
        self.entry_sugu.delete(0, tk.END)
        self.entry_pilt.delete(0, tk.END)

        messagebox.showinfo("Info", "Lemmikloom lisatud!")

    def kuva_lemmikloomad(self):
        kuva_lemmikloomad_aken = tk.Toplevel(self.root)
        kuva_lemmikloomad_aken.title("Lemmikloomade Nimekiri")

        for lemmiklooma_andmed in self.lemmikloomad:
            lemmiklooma_id, nimi, liik, vanus, sugu, pilt = lemmiklooma_andmed
            lemmiklooma_info = f"ID: {lemmiklooma_id}, Nimi: {nimi}, Liik: {liik}, Vanus: {vanus}, Sugu: {sugu}, Pilt: {pilt}"

            # Lae ja kuvab pilt, kui see eksisteerib
            pildi_tee = os.path.join(os.getcwd(), "pildid", pilt)
            if os.path.exists(pildi_tee):
                pilt_objekt = Image.open(pildi_tee)
                pilt_objekt.thumbnail((100, 100))  # Kohanda vastavalt vajadusele
                tk_pilt = ImageTk.PhotoImage(pilt_objekt)
                self.photo_images.append(tk_pilt)  # Säilita PhotoImage, et see ei häviks
                tk.Label(kuva_lemmikloomad_aken, text=lemmiklooma_info, image=tk_pilt).pack()
            else:
                tk.Label(kuva_lemmikloomad_aken, text=lemmiklooma_info).pack()

    def salvesta_andmed(self):
        # Vali faili salvestamise koht
        salvestamise_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if salvestamise_path:
            with open(salvestamise_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                # Kirjuta päisekirje
                writer.writerow(["ID", "Nimi", "Liik", "Vanus", "Sugu", "Pilt"])
                # Kirjuta andmed
                writer.writerows(self.lemmikloomad)

            messagebox.showinfo("Info", "Andmed on edukalt salvestatud!")

    def kustuta_lemmikloom(self):
        kustutamise_id = simpledialog.askinteger("Kustuta Lemmikloom", "Sisesta Lemmiklooma ID, mida soovid kustutada:")
        
        if kustutamise_id:
            lemmikloom = next((item for item in self.lemmikloomad if item[0] == kustutamise_id), None)
            
            if lemmikloom:
                self.lemmikloomad.remove(lemmikloom)
                messagebox.showinfo("Info", "Lemmikloom on edukalt kustutatud!")
            else:
                messagebox.showerror("Viga", f"Lemmikloom ID-ga {kustutamise_id} ei leitud.")

    def lisa_uuenda_pilt(self):
        lemmiklooma_id = simpledialog.askinteger("Lisa/Uuenda Pilt", "Sisesta Lemmiklooma ID, kellele soovid lisada/uuendada pilti:")
        if lemmiklooma_id:
            pildi_failitee = filedialog.askopenfilename(filetypes=[("Pildi failid", "*.png;*.jpg;*.jpeg;*.gif")])

            if pildi_failitee:
                # Kopeeri pilt pildikausta
                sihtkaust = os.path.join(os.getcwd(), "pildid")
                if not os.path.exists(sihtkaust):
                    os.makedirs(sihtkaust)

                sihtfail = os.path.join(sihtkaust, os.path.basename(pildi_failitee))
                shutil.copy(pildi_failitee, sihtfail)

                # Lisa pildi failinimi lemmiklooma andmetesse
                for lemmiklooma_andmed in self.lemmikloomad:
                    if lemmiklooma_andmed[0] == lemmiklooma_id:
                        lemmiklooma_andmed[-1] = os.path.basename(pildi_failitee)
                        break

                messagebox.showinfo("Info", "Pilt on edukalt lisatud/uuendatud!")

# Loome Tkinteri akna ja rakenduse instantsi
root = tk.Tk()
app = LemmikloomadeVarjupaik(root)
# Käivitame Tkinteri põhiloopi
root.mainloop()
