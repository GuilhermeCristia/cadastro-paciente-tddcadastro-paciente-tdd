import re
from datetime import datetime

class Paciente:
    def __init__(self, nome_completo, data_nascimento, cpf, telefone, genero, email):
        """Inicializa um paciente com todos os dados obrigatórios validados"""
        self.nome_completo = self.validar_nome_completo(nome_completo)
        self.data_nascimento = self.validar_data_nascimento(data_nascimento)
        self.cpf = self.validar_cpf(cpf)
        self.telefone = self.validar_telefone(telefone)
        self.genero = self.validar_genero(genero)
        self.email = self.validar_email(email)
    
    def validar_nome_completo(self, nome):
        """Valida se o nome contém pelo menos nome e sobrenome"""
        nome = nome.strip()
        if len(nome.split()) < 2:
            raise ValueError("Nome completo deve conter pelo menos nome e sobrenome")
        if len(nome) < 5:
            raise ValueError("Nome completo muito curto")
        return nome
    
    def validar_data_nascimento(self, data_str):
        """Valida a data de nascimento no formato YYYY-MM-DD"""
        try:
            data = datetime.strptime(data_str, "%Y-%m-%d").date()
            if data > datetime.now().date():
                raise ValueError("Data de nascimento não pode ser no futuro")
            return data_str
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato YYYY-MM-DD")
        
    # Fase GREEN (Implementação mínima)
    # Implementação inicial apenas para fazer o teste passar
    def validar_cpf(self, cpf):
        """Valida o CPF, removendo formatação e verificando tamanho"""
        cpf = re.sub(r'[^0-9]', '', cpf)
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos")
        return cpf
    
    def validar_telefone(self, telefone):
        """Valida o formato básico do telefone"""
        telefone = re.sub(r'[^0-9]', '', telefone)
        if len(telefone) not in (10, 11):
            raise ValueError("Telefone deve conter 10 ou 11 dígitos")
        return telefone
    
    def validar_genero(self, genero):
        """Valida os valores aceitos para gênero"""
        generos_aceitos = ["Masculino", "Feminino", "Outro", "Prefiro não informar"]
        if genero not in generos_aceitos:
            raise ValueError(f"Gênero deve ser um dos: {', '.join(generos_aceitos)}")
        return genero
    
    # Fase REFACTOR (Melhoria do código)
    # Versão refatorada da validação de email com regex otimizado
    def validar_email(self, email):
        """Valida o formato básico de email"""
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("Email inválido")
        return email
    
    def validar_cpf(self, cpf):
        """Versão REFACTOR: Validação robusta com regex e limpeza de dados"""
        cpf_limpo = re.sub(r'[^0-9]', '', cpf)  # Remove tudo que não for dígito
    
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve ter 11 dígitos")
    
        # Verifica dígitos repetidos (ex: 111.111.111-11)
        if cpf_limpo == cpf_limpo[0] * 11:
            raise ValueError("CPF inválido (dígitos repetidos)")
    
        return cpf_limpo
    
    def __str__(self):
        """Representação em string do paciente"""
        return f"Paciente: {self.nome_completo} ({self.cpf})"