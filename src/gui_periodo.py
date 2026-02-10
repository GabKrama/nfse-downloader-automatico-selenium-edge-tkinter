import tkinter as tk
from tkinter import messagebox
from datetime import date

def pedir_periodo_usuario():
    """
    Janela Tkinter para seleção de Data Inicial e Data Final,
    com auto-avanço e validação.
    """
    resultado = {"ini": None, "fim": None}

    def apenas_numeros(var, limite, proximo=None):
        texto = "".join(c for c in var.get() if c.isdigit())[:limite]
        var.set(texto)
        if len(texto) == limite and proximo:
            proximo.focus_set()

    def confirmar():
        try:
            ini = date(int(ano_ini.get()), int(mes_ini.get()), int(dia_ini.get()))
            fim = date(int(ano_fim.get()), int(mes_fim.get()), int(dia_fim.get()))
            if ini > fim:
                messagebox.showerror("Erro", "A data inicial é maior que a final.")
                return
            resultado["ini"] = ini
            resultado["fim"] = fim
            root.destroy()
        except:
            messagebox.showerror("Erro", "Preencha datas válidas.")

    root = tk.Tk()
    root.title("Selecionar Período")
    root.geometry("360x200")
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    dia_ini = tk.StringVar(); mes_ini = tk.StringVar(); ano_ini = tk.StringVar()
    dia_fim = tk.StringVar(); mes_fim = tk.StringVar(); ano_fim = tk.StringVar()

    tk.Label(frame, text="Data inicial").grid(row=0, column=0, columnspan=5)
    e_dia_ini = tk.Entry(frame, width=2, textvariable=dia_ini)
    e_mes_ini = tk.Entry(frame, width=2, textvariable=mes_ini)
    e_ano_ini = tk.Entry(frame, width=4, textvariable=ano_ini)
    e_dia_ini.grid(row=1, column=0)
    tk.Label(frame, text="/").grid(row=1, column=1)
    e_mes_ini.grid(row=1, column=2)
    tk.Label(frame, text="/").grid(row=1, column=3)
    e_ano_ini.grid(row=1, column=4)

    dia_ini.trace_add("write", lambda *_: apenas_numeros(dia_ini, 2, e_mes_ini))
    mes_ini.trace_add("write", lambda *_: apenas_numeros(mes_ini, 2, e_ano_ini))
    ano_ini.trace_add("write", lambda *_: apenas_numeros(ano_ini, 4))

    tk.Label(frame, text="Data final").grid(row=2, column=0, columnspan=5)
    e_dia_fim = tk.Entry(frame, width=2, textvariable=dia_fim)
    e_mes_fim = tk.Entry(frame, width=2, textvariable=mes_fim)
    e_ano_fim = tk.Entry(frame, width=4, textvariable=ano_fim)
    e_dia_fim.grid(row=3, column=0)
    tk.Label(frame, text="/").grid(row=3, column=1)
    e_mes_fim.grid(row=3, column=2)
    tk.Label(frame, text="/").grid(row=3, column=3)
    e_ano_fim.grid(row=3, column=4)

    dia_fim.trace_add("write", lambda *_: apenas_numeros(dia_fim, 2, e_mes_fim))
    mes_fim.trace_add("write", lambda *_: apenas_numeros(mes_fim, 2, e_ano_fim))
    ano_fim.trace_add("write", lambda *_: apenas_numeros(ano_fim, 4))

    tk.Button(frame, text="Confirmar", command=confirmar)\
        .grid(row=4, column=0, columnspan=5, pady=10)

    root.mainloop()

    if not resultado["ini"]:
        raise SystemExit("Execução cancelada pelo usuário.")

    return resultado["ini"], resultado["fim"]
``
