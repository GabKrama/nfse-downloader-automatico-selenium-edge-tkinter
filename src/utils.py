from datetime import date
from dateutil.tz import gettz

TZ = gettz("America/Sao_Paulo")

def normalize_cnpj(cnpj: str) -> str:
    """Remove caracteres não numéricos de um CNPJ."""
    return "".join(ch for ch in cnpj if ch.isdigit())

def br_date(d: date) -> str:
    """Formata a data no padrão brasileiro DD/MM/AAAA."""
    return d.strftime("%d/%m/%Y")
