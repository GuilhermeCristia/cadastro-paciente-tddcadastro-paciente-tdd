import unittest
from src.paciente import Paciente

class TestPaciente(unittest.TestCase):
    # Fase RED 
    # Teste escrito antes da implementação para validar a criação de paciente
    def test_criacao_paciente_valido(self):
        paciente = Paciente(
            nome_completo="João da Silva",
            data_nascimento="1990-05-15",
            cpf="123.456.789-00",
            telefone="(11) 99999-9999",
            genero="Masculino",
            email="joao@example.com"
        )
        
        self.assertEqual(paciente.nome_completo, "João da Silva")
        self.assertEqual(paciente.data_nascimento, "1990-05-15")
        self.assertEqual(paciente.cpf, "12345678900")
        self.assertEqual(paciente.telefone, "11999999999")
        self.assertEqual(paciente.genero, "Masculino")
        self.assertEqual(paciente.email, "joao@example.com")
    # Teste - Validação de CPF (RED)
    def test_cpf_invalido(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome_completo="Maria Oliveira",
                data_nascimento="1985-08-20",
                cpf="123.456.789", # Inválido
                telefone="(21) 98888-8888",
                genero="Feminino",
                email="maria@example.com"
            )
    # Teste - Validação de Email (RED)
    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome_completo="Carlos Souza",
                data_nascimento="1978-11-30",
                cpf="987.654.321-00",
                telefone="(31) 97777-7777",
                genero="Masculino",
                email="carlos.example.com" # Inválido
            )
    # Teste - Validação de data de Nascimento (RED)
    def test_data_nascimento_invalida(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome_completo="Ana Costa",
                data_nascimento="30-02-2000", # Inválido
                cpf="111.222.333-44",
                telefone="(41) 96666-6666",
                genero="Feminino",
                email="ana@example.com"
            )
    # Teste - Validação de Nome Completo (RED)
    def test_nome_completo_invalido(self):
        with self.assertRaises(ValueError):
            Paciente(
                nome_completo="João", # Inválido
                data_nascimento="1995-07-10",
                cpf="555.666.777-88",
                telefone="(51) 95555-5555",
                genero="Masculino",
                email="joao2@example.com"
            )
    # Teste - Validação de telefone (RED)
    def test_telefone_invalido(self):
        with self.assertRaises(ValueError):
         Paciente(
                nome_completo="Teste",
                data_nascimento="2000-01-01",
                cpf="123.456.789-09",
                telefone="123",  # Inválido
                genero="Masculino",
                email="teste@teste.com"
            )
         
if __name__ == '__main__':
    unittest.main()
    