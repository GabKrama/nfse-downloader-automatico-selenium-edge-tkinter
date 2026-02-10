import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import normalize_cnpj, br_date

BASE_URL = "https://exemplo.gov.br/PortalNFSe/"

def wait_click(driver, by, sel, timeout=7):
    el = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, sel)))
    el.click()
    return el

def wait_visible(driver, by, sel, timeout=7):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, sel)))

# --------------------------------------------
# LOGIN
# --------------------------------------------

def navegar_para_login(driver):
    driver.get(BASE_URL)
    return wait_visible(driver, By.ID, "campo_cnpj", 10)

def login(driver, cnpj, senha):
    campo = navegar_para_login(driver)
    campo.send_keys(normalize_cnpj(cnpj))

    campo_senha = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    campo_senha.send_keys(senha)

    wait_click(driver, By.XPATH, "//button[contains(.,'Entrar')]")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# --------------------------------------------
# NOTAS RECEBIDAS / FILTRO / DOWNLOAD
# --------------------------------------------

def ir_para_notas(driver):
    wait_click(driver, By.XPATH, "//a[contains(.,'Notas Recebidas')]")

def preencher_datas(driver, dt_ini, dt_fim):
    campo_ini = wait_visible(driver, By.ID, "datainicio")
    campo_fim = wait_visible(driver, By.ID, "datafim")

    campo_ini.clear()
    campo_ini.send_keys(br_date(dt_ini))

    campo_fim.clear()
    campo_fim.send_keys(br_date(dt_fim))

def clicar_filtrar(driver):
    wait_click(driver, By.XPATH, "//button[contains(.,'Filtrar')]")
    time.sleep(0.5)

def baixar_todos(driver, processed):
    total = 0
    icones = driver.find_elements(By.CSS_SELECTOR, "i.glyphicon.glyphicon-option-vertical")

    for icone in icones:
        icone.click()
        link = driver.find_element(By.XPATH, "//a[contains(@href,'Download')]")
        href = link.get_attribute("href")

        if href not in processed:
            processed.add(href)
            link.click()
            total += 1

    return total

def proxima_pagina(driver):
    try:
        btn = driver.find_element(By.XPATH, "//a[@title='Próxima']")
        if btn.get_attribute("href") and not btn.get_attribute("href").endswith("#"):
            btn.click()
            return True
    except:
        return False
    return False

def baixar_periodo(driver, dt_ini, dt_fim):
    ir_para_notas(driver)
    preencher_datas(driver, dt_ini, dt_fim)
    clicar_filtrar(driver)

    processed = set()
    total = 0

    while True:
        total += baixar_todos(driver, processed)
        if not proxima_pagina(driver):
            break

    return total
