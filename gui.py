import tkinter as tk
from tkinter import messagebox
from downloader import baixar_playlist

def iniciar_interface():
    root = tk.Tk()
    root.title("Baixar Músicas do YouTube")
    root.geometry("450x150")

    lbl = tk.Label(root, text="Link da playlist ou vídeo:", font=("Arial", 10))
    lbl.pack(pady=10)
    
    entry_link = tk.Entry(root, width=50, font=("Arial", 10))
    entry_link.pack(pady=5)

    def on_click_baixar():
        link = entry_link.get()
        if link.strip():
            btn_baixar.config(state=tk.DISABLED)
            root.update()
            try:
                baixar_playlist(link)
                messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro durante o download:\n{e}")
            finally:
                btn_baixar.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um link válido.")

    btn_baixar = tk.Button(root, text="Baixar", command=on_click_baixar, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white")
    btn_baixar.pack(pady=10)

    root.mainloop()
