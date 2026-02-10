# NFSe Downloader Automático (Selenium + Edge + Tkinter)

Automação completa para download de Notas Fiscais de Serviço Eletrônicas (NFSe)
em portais públicos, utilizando:

- 🖥️ **Interface gráfica (Tkinter)** para selecionar período com auto‑avanço  
- 🧭 **Selenium + Edge WebDriver** para navegação  
- 🔄 **Paginação automática** com prevenção contra downloads repetidos  
- 🧰 **Execução como .py ou .exe (PyInstaller)**  
- 🛡️ **Versão 100% genérica** para uso educacional e portfólio (sem dados reais)

Este projeto demonstra um fluxo completo e profissional de automação web,
incluindo tratamento de erros, persistência de sessão, fallback de perfil e
estrutura robusta para raspagem/extração de documentos.

---
## 🚀 Tecnologias utilizadas

| Tecnologia | Função |
|-----------|--------|
| **Python 3.10+** | Linguagem principal |
| **Tkinter** | Interface gráfica para entrada de datas |
| **Selenium WebDriver** | Automação do navegador |
| **Microsoft Edge WebDriver** | Navegador utilizado |
| **PyInstaller** | Empacotamento para .exe |

---
## 📷 Demonstração (UI do Período)

A interface solicita ao usuário:

- Dia / Mês / Ano inicial  
- Dia / Mês / Ano final  
- Auto‑avanço ao completar os campos  
- Validação de datas reais  

---

## 📁 Estrutura do Projeto
NFSe-Automation/
│
├── src/
│   ├── main.py                 # Script principal (automatiza todo o fluxo)
│   ├── gui_periodo.py          # Interface Tkinter modularizada
│   ├── browser_setup.py        # Configuração do Edge WebDriver
│   ├── portal_actions.py       # Funções de login, navegação e download
│   └── utils.py                # Funções auxiliares
│
├── drivers/
│   └── msedgedriver.exe        # Driver necessário para execução
│
├── README.md
├── LICENSE
└── requirements.txt
