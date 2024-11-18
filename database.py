import datetime  # Importa o módulo datetime para manipular datas

class DataBase:
    def __init__(self, filename):
        self.filename = filename  # Nome do arquivo que armazenará os dados dos usuários
        self.users = None  # Dicionário para armazenar os dados dos usuários
        self.file = None  # Variável que irá referenciar o arquivo de dados
        self.load()  # Carrega os dados dos usuários do arquivo

    def load(self):
        # Abre o arquivo em modo leitura
        self.file = open(self.filename, 'r')
        self.users = {}  # Inicializa o dicionário de usuários

        # Lê cada linha do arquivo e popula o dicionário de usuários
        for line in self.file:
            # Divide a linha nos diferentes campos usando ';' como separador
            email, password, name, created = line.strip().split(';')
            self.users[email] = (password, name, created)  # Armazena os dados no dicionário com o email como chave

        self.file.close()  # Fecha o arquivo

    def get_user(self, email):
        # Verifica se o email existe no dicionário de usuários e retorna os dados do usuário
        if email in self.users:
            return self.users[email]
        else:
            return -1  # Retorna -1 se o email não estiver cadastrado

    def add_user(self, email, password, name):
        # Verifica se o email já está registrado
        if email.strip() not in self.users:
            # Adiciona o usuário ao dicionário, incluindo a data atual
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()  # Salva o dicionário atualizado no arquivo
            return 1  # Retorna 1 para indicar sucesso na criação do usuário
        else:
            print('O Email já existe')  # Exibe mensagem de erro se o email já estiver cadastrado
            return -1  # Retorna -1 para indicar falha na criação

    def validate(self, email, password):
        # Verifica se o usuário existe e se a senha está correta
        if self.get_user(email) != -1:
            return self.users[email][0] == password  # Retorna True se a senha coincidir
        else:
            return False  # Retorna False se o usuário não existir ou a senha estiver incorreta

    def save(self):
        # Salva todos os usuários no arquivo, sobrescrevendo o conteúdo existente
        with open(self.filename, 'w') as f:
            for user in self.users:
                # Escreve os dados do usuário no formato 'email;senha;nome;data'
                f.write(user + ';' + self.users[user][0] + ';' + self.users[user][1] + ';' + self.users[user][2] + '\n')

    @staticmethod
    def get_date():
        # Retorna a data atual no formato 'AAAA-MM-DD'
        return str(datetime.datetime.now()).split(' ')[0]
