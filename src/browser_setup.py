import os
import sys
import tempfile
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

def get_edge_driver_path():
    """Retorna o caminho do driver, compatível com script e .exe."""
    if getattr(sys, "frozen", False):  
        base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "..", "drivers", "msedgedriver.exe")

EDGE_DRIVER_PATH = get_edge_driver_path()

def build_options(user_data_dir=None, profile=None):
    opts = EdgeOptions()
    if user_data_dir:
        opts.add_argument(f"--user-data-dir={user_data_dir}")
    if profile:
        opts.add_argument(f"--profile-directory={profile}")
    opts.add_argument("--start-maximized")
    opts.add_argument("--remote-allow-origins=*")
    opts.set_capability("pageLoadStrategy", "eager")
    return opts

def setup_edge():
    """Tenta usar perfil real; fallback para perfil temporário."""
    user_data_dir = os.path.expanduser("~/AppData/Local/Microsoft/Edge/User Data")
    profile = "Default"

    try:
        return webdriver.Edge(
            service=EdgeService(EDGE_DRIVER_PATH),
            options=build_options(user_data_dir, profile)
        )
    except:
        tmp_dir = tempfile.mkdtemp(prefix="edge_tmp_")
        print(f"[INFO] Usando perfil temporário: {tmp_dir}")
        return webdriver.Edge(
            service=EdgeService(EDGE_DRIVER_PATH),
            options=build_options(tmp_dir, None)
        )
