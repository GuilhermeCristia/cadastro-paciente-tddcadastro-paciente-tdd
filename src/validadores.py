import re
from datetime import datetime

def validar_cpf(cpf: str) -> str:
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11:
        raise ValueError("CPF deve conter 11 dígitos")
    return cpf

def validar_email(email: str) -> str:
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Email inválido")
    return email