import random

class Alunos:
    alunos = {}
    matricula_auto = 1000

    def __init__(self, nome, matricula, notas=None, idade=None, curso=None, cpf=None, senha=None):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.idade = idade
        self.curso = curso
        self.cpf = cpf
        self.senha = senha

    @staticmethod
    def calcular_media(p1, p2, trabalho):
        return (p1 * 4 + p2 * 4 + trabalho * 2) / 10

    @staticmethod
    def situacao_aluno(media):
        if media > 10 or media < 0:
            return "Nota inválida, tente novamente"
        elif media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    @classmethod
    def cadastrar_aluno(cls):
        print("\n--- Cadastro de Notas ---")
        matricula = input("Digite o número da matrícula: ").strip()
        if matricula not in cls.alunos:
            print("Matrícula não encontrada. O aluno precisa estar matriculado primeiro.")
            return

        try:
            p1 = float(input("Digite a nota da P1: "))
            p2 = float(input("Digite a nota da P2: "))
            trabalho = float(input("Digite a nota do Trabalho: "))
        except ValueError:
            print("Digite apenas números válidos.")
            return

        # Validação de notas
        if any(nota > 10 or nota < 0 for nota in [p1, p2, trabalho]):
            print("Notas inválidas! As notas devem estar entre 0 e 10.")
            return

        media = cls.calcular_media(p1, p2, trabalho)
        situacao = cls.situacao_aluno(media)

        cls.alunos[matricula]["Notas"] = {"P1": p1, "P2": p2, "Trabalho": trabalho}
        cls.alunos[matricula]["Média"] = round(media, 2)
        cls.alunos[matricula]["Situação"] = situacao

        print(f"\nNotas cadastradas com sucesso!")
        print(f"Média final: {media:.2f} - Situação: {situacao}\n")

    @classmethod
    def acessar_aluno(cls):
        print("\n--- Acesso do Aluno ---")
        matricula = input("Digite sua matrícula: ").strip()
        senha = input("Digite sua senha: ").strip()

        if matricula in cls.alunos and cls.alunos[matricula]["Senha"] == senha:
            dados = cls.alunos[matricula]
            print(f"\nAluno: {dados['Nome']}")
            print(f"CPF: {dados['CPF']}")
            print(f"Curso: {dados['Curso']}")
            print(f"Idade: {dados['Idade']}")
            if "Notas" in dados:
                print(f"Notas: {dados['Notas']}")
                print(f"Média: {dados['Média']}")
                print(f"Situação: {dados['Situação']}")
            else:
                print("Notas ainda não lançadas.")
        else:
            print("Matrícula ou senha incorretas.\n")

    @classmethod
    def matricular_aluno(cls):
        print("\n--- Matrícula de Novo Aluno ---")

        while True:
            nome = input("Digite seu nome completo: ").strip()
            if nome.replace(" ", "").isalpha():
                break
            print("Digite apenas letras!")

        while True:
            try:
                idade = int(input("Digite sua idade: "))
                if idade >= 18:
                    break
                else:
                    print("Apenas maiores de 18 anos podem se matricular.")
            except ValueError:
                print("Digite uma idade válida.")

        while True:
            cpf = input("Digite seu CPF (apenas números): ").strip()
            if not (cpf.isdigit() and len(cpf) == 11):
                print("CPF inválido. Digite exatamente 11 números.")
                continue

            # Verifica se o CPF já está cadastrado
            if any(aluno["CPF"] == cpf for aluno in cls.alunos.values()):
                print("CPF já cadastrado! Cada aluno deve ter um CPF único.")
                continue

            break

        print("\nEscolha seu curso:")
        cursos = {
            "1": "Ciência da Computação",
            "2": "Administração",
            "3": "Engenharia Civil",
            "4": "Psicologia"
        }

        for chave, valor in cursos.items():
            print(f"{chave}. {valor}")

        while True:
            escolha = input("Número do curso: ").strip()
            if escolha in cursos:
                curso_escolhido = cursos[escolha]
                break
            else:
                print("Escolha inválida.")

        matricula = str(cls.matricula_auto)
        cls.matricula_auto += 1

        senha = str(random.randint(10000, 99999))

        cls.alunos[matricula] = {
            "Nome": nome,
            "Idade": idade,
            "CPF": cpf,
            "Curso": curso_escolhido,
            "Senha": senha
        }

        print("\n--- Matrícula Concluída ---")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"CPF: {cpf}")
        print(f"Curso: {curso_escolhido}")
        print(f"Sua matrícula é: {matricula}")
        print(f"Sua senha de acesso é: {senha} (guarde bem!)\n")

    @staticmethod
    def central_ajuda():
        while True:
            print("\n--- Central de Ajuda ---")
            print("1. Como me matricular")
            print("2. Como ver minhas notas")
            print("3. Quais as unidades disponíveis")
            print("4. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                print("""
Para se matricular, volte ao menu principal e selecione a opção 2 (Quero me matricular).
Em seguida, informe seu nome, idade e CPF.
O sistema irá gerar automaticamente o número da sua matrícula e uma senha de acesso.
Depois disso, basta fazer login usando sua matrícula e senha para acessar suas informações.
""")
            elif opcao == "2":
                print("""
Se você já é aluno, escolha a opção 1 (Sou aluno) no menu principal.
Digite sua matrícula e senha para visualizar suas notas, média e situação acadêmica.
""")
            elif opcao == "3":
                print("""
Unidades disponíveis:
- São Paulo (SP)
- Rio de Janeiro (RJ)
- Belo Horizonte (MG)
- Curitiba (PR)
""")
            elif opcao == "4":
                print("Voltando ao menu principal...\n")
                break
            else:
                print("Opção inválida, tente novamente.")

    @classmethod
    def menu(cls):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1. Sou aluno")
            print("2. Quero me matricular")
            print("3. Central de ajuda")
            print("4. Cadastrar notas")
            print("5. Sair")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                cls.acessar_aluno()
            elif escolha == "2":
                cls.matricular_aluno()
            elif escolha == "3":
                cls.central_ajuda()
            elif escolha == "4":
                cls.cadastrar_aluno()
            elif escolha == "5":
                print("Saindo... Até logo!")
                break
            else:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    Alunos.menu()
