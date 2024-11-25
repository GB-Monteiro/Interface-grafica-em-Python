<h1 align="center">Projeto de Interface Gráfica com Python e Kivy</h1>
Este é um projeto de interface gráfica (GUI) desenvolvido utilizando Python com a biblioteca Kivy para a construção de telas interativas. O sistema permite que usuários criem contas e façam login, com os dados armazenados em um arquivo local (userx.txt).

# 📸 Captura de Tela
![Imagem Interface Gráfica Python](https://github.com/user-attachments/assets/112d9b0f-f8aa-460e-865c-54b678b096e2)
![Imagem 2 Interface Gráfica Python](https://github.com/user-attachments/assets/875fb7d0-c20a-43cd-9fc2-2c12863ce0ce)

# 📋 Funcionalidades
Tela de Login:

- Campos para e-mail e senha.

- Botão para realizar login.

- Mensagem de erro para entradas inválidas.

Tela de Criação de Conta:

- Permite cadastrar um novo usuário.

- Validações básicas para entradas.

Gerenciamento de Usuários:

- Armazena os dados de e-mail e senha no arquivo userx.txt dentro da pasta do projeto.

# 🛠️ Tecnologias Utilizadas
Python: Linguagem principal do projeto.

Kivy: Framework para construção de interfaces gráficas modernas e responsivas.

Banco de Dados Local: Utilização de um arquivo .txt para simular o armazenamento de dados.

# 📂 Estrutura do Projeto
```
📂 kivy_project
├── database.py            # Lógica para manipulação do banco de dados local.
├── main.py                # Arquivo principal que executa a aplicação.
├── my.kv                  # Arquivo de layout em Kivy (design da interface).
├── users.txt              # Arquivo usado como banco de dados local.
└── __pycache__/           # Cache gerado automaticamente pelo Python.
```
# 🚀 Como Executar o Projeto
Clone o repositório (ou faça o download dos arquivos):
```
git clone https://github.com/GB-Monteiro/Interface-grafica-em-Python.git
cd MeuProjeto
```
Certifique-se de que o Python 3.x está instalado e instale o Kivy:
```
pip install kivy
````
Execute o projeto:
```
python main.py
```
Interaja com a aplicação.

Use a interface para criar uma conta.

Faça login com as credenciais criadas.

# ⚙️ Configurações e Arquivo de Banco de Dados

O arquivo userx.txt armazena as informações dos usuários no seguinte formato:
```
email;senha;nome;data_de_criacao
```
Caso o arquivo não exista, ele será criado automaticamente ao rodar o programa.

# 🧑‍💻 Autor

Gabriel Monteiro Siqueira: Desenvolvedor do projeto.

https://www.linkedin.com/in/gabriel-monteiro-187219246/

# 📄 Licença

Este projeto é de uso livre. Sinta-se à vontade para estudar, modificar e reutilizar.
