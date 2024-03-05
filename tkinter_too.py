import tkinter as tk
from tkinter import messagebox, filedialog
import csv
from PIL import Image, ImageTk

class Lemmikloom:
    def __init__(self, id, nimi, liik, vanus, sugu, pilt_path):
        self.id = id
        self.nimi = nimi
        self.liik = liik
        self.vanus = vanus
        self.sugu = sugu
        self.pilt_path = pilt_path
        self.pilt_objekt = None

class LemmikloomadeVarjupaik:
    def __init__(self):
        self.lemmikloomad = []
        self.loendur = 1

    def lisa_lemmikloom(self, nimi, liik, vanus, sugu, pilt_path):
        lemmikloom = Lemmikloom(self.loendur, nimi, liik, vanus, sugu, pilt_path)
        lemmikloom.pilt_objekt = self.laadi_pilt(lemmikloom.pilt_path)
        self.lemmikloomad.append(lemmikloom)
        self.loendur += 1

    def laadi_pilt(self, pilt_path):
        pilt = Image.open(pilt_path)
        pilt.thumbnail((150, 150))
        return ImageTk.PhotoImage(pilt)

    def leia_lemmikloom(self, otsing):
        tulemused = []
        for lemmikloom in self.lemmikloomad:
            if otsing.lower() in lemmikloom.nimi.lower() or otsing.lower() == str(lemmikloom.id):
                tulemused.append(lemmikloom)
        return tulemused

    def muuda_lemmiklooma_andmeid(self, lemmikloom, nimi, liik, vanus, sugu, pilt_path):
        lemmikloom.nimi = nimi
        lemmikloom.liik = liik
        lemmikloom.vanus = vanus
        lemmikloom.sugu = sugu
        if pilt_path:
            lemmikloom.pilt_path = pilt_path
            lemmikloom.pilt_objekt = self.laadi_pilt(pilt_path)

    def kustuta_lemmikloom(self, lemmikloom):
        self.lemmikloomad.remove(lemmikloom)

    def salvesta_andmed(self, failinimi):
        with open(failinimi, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nimi', 'Liik', 'Vanus', 'Sugu', 'Pilt_Path'])
            for lemmikloom in self.lemmikloomad:
                writer.writerow([lemmikloom.id, lemmikloom.nimi, lemmikloom.liik, lemmikloom.vanus, lemmikloom.sugu, lemmikloom.pilt_path])

    def lae_andmed(self, failinimi):
        self.lemmikloomad = []
        try:
            with open(failinimi, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Ignore header row
                for row in reader:
                    id, nimi, liik, vanus, sugu, pilt_path = row
                    self.lisa_lemmikloom(nimi, liik, vanus, sugu, pilt_path)
        except FileNotFoundError:
            pass

class Rakendus:
    def __init__(self, root):
        self.root = root
        self.root.title("Lemmikloomade Varjupaik")

        self.varjupaik = LemmikloomadeVarjupaik()

        # Kasutajaliides
        self.loo_kasutajaliides()

    def loo_kasutajaliides(self):
        # Sisestuse väljad
        self.nimi_label = tk.Label(self.root, text="Nimi:")
        self.nimi_label.grid(row=0, column=0, padx=10, pady=5)
        self.nimi_entry = tk.Entry(self.root, width=30)
        self.nimi_entry.grid(row=0, column=1, padx=10, pady=5)

        self.liik_label = tk.Label(self.root, text="Liik:")
        self.liik_label.grid(row=1, column=0, padx=10, pady=5)
        self.liik_entry = tk.Entry(self.root, width=30)
        self.liik_entry.grid(row=1, column=1, padx=10, pady=5)

        self.vanus_label = tk.Label(self.root, text="Vanus:")
        self.vanus_label.grid(row=2, column=0, padx=10, pady=5)
        self.vanus_entry = tk.Entry(self.root, width=30)
        self.vanus_entry.grid(row=2, column=1, padx=10, pady=5)

        self.sugu_label = tk.Label(self.root, text="Sugu:")
        self.sugu_label.grid(row=3, column=0, padx=10, pady=5)
        self.sugu_entry = tk.Entry(self.root, width=30)
        self.sugu_entry.grid(row=3, column=1, padx=10, pady=5)

        # Pildi valimise nupp
        self.pilt_nupp = tk.Button(self.root, text="Lisa Pilt", command=self.vali_pilt)
        self.pilt_nupp.grid(row=4, column=0, padx=10, pady=5)

        # Andmete lisamise nupp
        self.lisa_nupp = tk.Button(self.root, text="Lisa Lemmikloom", command=self.lisa_lemmikloom)
        self.lisa_nupp.grid(row=4, column=1, padx=10, pady=5)

        # Otsingu väljad ja nupp
        self.otsing_label = tk.Label(self.root, text="Otsing:")
        self.otsing_label.grid(row=0, column=4, padx=10, pady=5)
        self.otsing_entry = tk.Entry(self.root, width=30)
        self.otsing_entry.grid(row=0, column=5, padx=10, pady=5)
        self.otsi_nupp = tk.Button(self.root, text="Otsi", command=self.otsi_lemmiklooma)
        self.otsi_nupp.grid(row=0, column=6, padx=10, pady=5)

        # Tulemused
        self.tulemused_listbox = tk.Listbox(self.root, height=10, width=50)
        self.tulemused_listbox.grid(row=1, column=4, rowspan=4, columnspan=3, padx=10, pady=5)

        # Kuvamise ala
        self.kuva_ala = tk.Label(self.root, text="Lemmiklooma Info Kuvamine", font=('Helvetica', 14, 'bold'))
        self.kuva_ala.grid(row=6, column=1, padx=10, pady=5)

        # Muutmise ja kustutamise nupp
        self.muuda_nupp = tk.Button(self.root, text="Muuda Andmeid", command=self.muuda_andmeid)
        self.muuda_nupp.grid(row=7, column=0, padx=10, pady=5)
        self.kustuta_nupp = tk.Button(self.root, text="Kustuta Lemmikloom", command=self.kustuta_lemmikloom)
        self.kustuta_nupp.grid(row=7, column=1, padx=10, pady=5)

        # Lae ja Salvesta nupud
        self.lae_nupp = tk.Button(self.root, text="Lae Andmed", command=self.lae_andmed)
        self.lae_nupp.grid(row=8, column=4, padx=10, pady=5)
        self.salvesta_nupp = tk.Button(self.root, text="Salvesta Andmed", command=self.salvesta_andmed)
        self.salvesta_nupp.grid(row=8, column=5, padx=10, pady=5)

    def vali_pilt(self):
        pilt_path = filedialog.askopenfilename(title="Vali Pilt", filetypes=[("Pildifailid", "*.png;*.jpg;*.jpeg;*.gif")])
        if pilt_path:
            self.pilt_path = pilt_path

    def lisa_lemmikloom(self):
        nimi = self.nimi_entry.get()
        liik = self.liik_entry.get()
        vanus = self.vanus_entry.get()
        sugu = self.sugu_entry.get()

        if hasattr(self, 'pilt_path'):
            self.varjupaik.lisa_lemmikloom(nimi, liik, vanus, sugu, self.pilt_path)
            self.pilt_path = None
            self.tuhjenda_sisestusvaljad()
            self.otsi_lemmiklooma()
            messagebox.showinfo("Info", "Lemmikloom on lisatud!")
        else:
            messagebox.showwarning("Hoiatus", "Palun lisage lemmikloomale pilt!")

    def otsi_lemmiklooma(self):
        otsing = self.otsing_entry.get()
        tulemused = self.varjupaik.leia_lemmikloom(otsing)

        self.tulemused_listbox.delete(0, tk.END)

        if not tulemused:
            self.tulemused_listbox.insert(tk.END, "Tulemused puuduvad")
        else:
            for lemmikloom in tulemused:
                self.tulemused_listbox.insert(tk.END, f"{lemmikloom.nimi} ({lemmikloom.liik}, {lemmikloom.sugu}, {lemmikloom.vanus} a)")

    def kuva_lemmiklooma_info(self, lemmikloom):
        info = f"Nimi: {lemmikloom.nimi}\nLiik: {lemmikloom.liik}\nVanus: {lemmikloom.vanus}\nSugu: {lemmikloom.sugu}"
        self.kuva_ala.config(text=info)

        # Kuvab lemmiklooma pildi
        if hasattr(self, 'pilt_label'):
            self.pilt_label.destroy()

        pilt_objekt = lemmikloom.pilt_objekt
        self.pilt_label = tk.Label(self.root, image=pilt_objekt)
        self.pilt_label.image = pilt_objekt
        self.pilt_label.grid(row=9, column=1, padx=10, pady=5)

    def muuda_andmeid(self):
        valitud_indeks = self.tulemused_listbox.curselection()
        if valitud_indeks:
            valitud_indeks = int(valitud_indeks[0])
            lemmikloom = self.varjupaik.lemmikloomad[valitud_indeks]

            nimi = self.nimi_entry.get()
            liik = self.liik_entry.get()
            vanus = self.vanus_entry.get()
            sugu = self.sugu_entry.get()

            if hasattr(self, 'pilt_path'):
                pilt_path = self.pilt_path
            else:
                pilt_path = lemmikloom.pilt_path

            self.varjupaik.muuda_lemmiklooma_andmeid(lemmikloom, nimi, liik, vanus, sugu, pilt_path)
            self.tuhjenda_sisestusvaljad()
            self.otsi_lemmiklooma()
            messagebox.showinfo("Info", "Andmed on muudetud!")
        else:
            messagebox.showwarning("Hoiatus", "Palun valige lemmikloom tulemuste loendist!")

    def kustuta_lemmikloom(self):
        valitud_indeks = self.tulemused_listbox.curselection()
        if valitud_indeks:
            valitud_indeks = int(valitud_indeks[0])
            lemmikloom = self.varjupaik.lemmikloomad[valitud_indeks]

            vastus = messagebox.askyesno("Kinnita kustutamine", f"Kas olete kindel, et soovite kustutada lemmiklooma {lemmikloom.nimi}?")
            if vastus:
                self.varjupaik.kustuta_lemmikloom(lemmikloom)
                self.tuhjenda_sisestusvaljad()
                self.otsi_lemmiklooma()
                messagebox.showinfo("Info", "Lemmikloom on kustutatud!")
        else:
            messagebox.showwarning("Hoiatus", "Palun valige lemmikloom tulemuste loendist!")

    def lae_andmed(self):
        failinimi = filedialog.askopenfilename(title="Lae Andmed", filetypes=[("CSV-failid", "*.csv")])
        if failinimi:
            self.varjupaik.lae_andmed(failinimi)
            self.otsi_lemmiklooma()
            messagebox.showinfo("Info", "Andmed on laetud!")

    def salvesta_andmed(self):
        failinimi = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV-failid", "*.csv")])
        if failinimi:
            self.varjupaik.salvesta_andmed(failinimi)
            messagebox.showinfo("Info", "Andmed on salvestatud!")

    def tuhjenda_sisestusvaljad(self):
        self.nimi_entry.delete(0, tk.END)
        self.liik_entry.delete(0, tk.END)
        self.vanus_entry.delete(0, tk.END)
        self.sugu_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    rakendus = Rakendus(root)
    root.mainloop()
