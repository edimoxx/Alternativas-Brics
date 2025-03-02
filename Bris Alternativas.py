import tkinter as tk
from tkinter import ttk, scrolledtext

# Dados das estratégias, alternativas e catalisadores
strategies_data = {
    "Comércio em Moedas Locais": {
        "alternativas": [
            "Acordos bilaterais entre Brasil e China para usar real e yuan.",
            "Negociações Índia-Rússia em rupia e rublo.",
            "Plataformas de câmbio digital para moedas locais."
        ],
        "catalisadores": [
            "Aumento do comércio intra-BRICs para 30% do global.",
            "Sanções ocidentais forçando alternativas ao dólar.",
            "Digitalização financeira nos BRICs."
        ]
    },
    "Diversificar Reservas": {
        "alternativas": [
            "Compra de ouro em larga escala por bancos centrais.",
            "Adoção de yuan como reserva secundária.",
            "Uso de criptomoedas lastreadas em ativos."
        ],
        "catalisadores": [
            "Queda da confiança no dólar devido a crises nos EUA.",
            "Expansão do PIB dos BRICs em PPC.",
            "Inflação global pressionando moedas fiduciárias."
        ]
    },
    "Moeda Comum": {
        "alternativas": [
            "Cesta de moedas com yuan, rublo e real.",
            "Moeda digital dos BRICs baseada em blockchain.",
            "Unidade de conta para comércio interno."
        ],
        "catalisadores": [
            "Cooperação política fortalecida entre BRICs.",
            "Tecnologia blockchain madura até 2040.",
            "Rejeição ao dólar em favor de soluções locais."
        ]
    },
    "Commodities em Outras Moedas": {
        "alternativas": [
            "Petróleo saudita precificado em yuan.",
            "Exportações de grãos ucranianos em rublo.",
            "Contratos futuros em moedas BRICs."
        ],
        "catalisadores": [
            "Controle de 40% da produção de petróleo pelos BRICs.",
            "Demanda chinesa por commodities em yuan.",
            "Fim de conflitos como a guerra na Ucrânia."
        ]
    },
    "Sistemas Financeiros Alternativos": {
        "alternativas": [
            "Expansão do CIPS chinês para todos os BRICs.",
            "Integração do SPFS russo com parceiros.",
            "Plataforma financeira própria dos BRICs."
        ],
        "catalisadores": [
            "Exclusão de países do SWIFT pelo Ocidente.",
            "Aumento das transações digitais globais.",
            "Parcerias com o Sul Global."
        ]
    },
    "Conversibilidade do Yuan": {
        "alternativas": [
            "Liberalização gradual do mercado de capitais chinês.",
            "Incentivos para uso do yuan em comércio global.",
            "Acordos internacionais para reservas em yuan."
        ],
        "catalisadores": [
            "Crescimento da economia chinesa acima de 5% ao ano.",
            "Estabilidade política na China.",
            "Declínio da confiança no dólar."
        ]
    },
    "Aproveitar Crises nos EUA": {
        "alternativas": [
            "Promoção de alternativas durante crises de dívida americana.",
            "Campanhas diplomáticas contra o dólar.",
            "Parcerias com países sancionados pelos EUA."
        ],
        "catalisadores": [
            "Default técnico da dívida dos EUA.",
            "Polarização política extrema nos EUA.",
            "Erros geopolíticos americanos."
        ]
    },
    "Influência Geopolítica": {
        "alternativas": [
            "Expansão dos BRICs com novos membros como Turquia.",
            "Acordos econômicos com a ASEAN e África.",
            "Fóruns alternativos ao G7."
        ],
        "catalisadores": [
            "Declínio da influência do G7.",
            "Aumento do soft power chinês e indiano.",
            "Rejeição global ao unilateralismo dos EUA."
        ]
    }
}

# Função para exibir resultados
def search_strategy():
    selected_strategy = strategy_var.get()
    result_text.delete(1.0, tk.END)
    
    if selected_strategy in strategies_data:
        data = strategies_data[selected_strategy]
        result_text.insert(tk.END, f"Estratégia: {selected_strategy}\n\n")
        result_text.insert(tk.END, "Alternativas:\n")
        for alt in data["alternativas"]:
            result_text.insert(tk.END, f"- {alt}\n")
        result_text.insert(tk.END, "\nCatalisadores:\n")
        for cat in data["catalisadores"]:
            result_text.insert(tk.END, f"- {cat}\n")
    else:
        result_text.insert(tk.END, "Selecione uma estratégia válida.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Motor de Busca: Estratégias dos BRICs contra o Dólar")
root.geometry("600x400")

# Label
label = tk.Label(root, text="Selecione uma Estratégia:", font=("Arial", 12))
label.pack(pady=10)

# Dropdown com as estratégias
strategy_var = tk.StringVar()
strategy_dropdown = ttk.Combobox(root, textvariable=strategy_var, values=list(strategies_data.keys()), width=50)
strategy_dropdown.pack(pady=10)
strategy_dropdown.set("Comércio em Moedas Locais")  # Valor padrão

# Botão de busca
search_button = tk.Button(root, text="Buscar", command=search_strategy, font=("Arial", 10))
search_button.pack(pady=10)

# Área de texto para resultados
result_text = scrolledtext.ScrolledText(root, width=70, height=20, font=("Arial", 10))
result_text.pack(pady=10)

# Iniciar a interface
root.mainloop()