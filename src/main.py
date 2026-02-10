from gui_periodo import pedir_periodo_usuario
from browser_setup import setup_edge
from portal_actions import login, baixar_periodo
from utils import br_date
import time

# Dados fictícios para portfólio
CNPJS = [
    {"cnpj": "00.000.000/0001-00", "sigla": "EMPRESA_A"},
    {"cnpj": "11.111.111/0001-11", "sigla": "EMPRESA_B"},
    {"cnpj": "22.222.222/0001-22", "sigla": "EMPRESA_C"},
]

NFSE_SENHA = "SENHA_EXEMPLO"

def run():
    dt_ini, dt_fim = pedir_periodo_usuario()
    print(f"Período: {br_date(dt_ini)} a {br_date(dt_fim)}")

    driver = setup_edge()
    try:
        for item in CNPJS:
            print(f"\n>>> {item['sigla']} ({item['cnpj']})")
            login(driver, item["cnpj"], NFSE_SENHA)

            total = baixar_periodo(driver, dt_ini, dt_fim)
            print(f"Downloads realizados: {total}")

            driver.get("about:blank")
            time.sleep(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run()
