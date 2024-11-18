from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        # Verifica se todos os campos estão preenchidos e o email tem um formato válido
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                # Adiciona o usuário ao banco de dados
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"  # Volta para a tela de login
            else:
                invalidForm()  # Exibe popup de formulário inválido
        else:
            invalidForm()  # Exibe popup de formulário inválido

    def login(self):
        # Limpa os campos e vai para a tela de login
        self.reset()
        sm.current = "login"

    def reset(self):
        # Limpa os campos de texto
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        # Verifica se as credenciais são válidas
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"  # Vai para a tela principal
        else:
            invalidLogin()  # Exibe popup de login inválido

    def createBtn(self):
        # Vai para a tela de criação de conta
        self.reset()
        sm.current = "create"

    def reset(self):
        # Limpa os campos de texto
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        # Desloga o usuário e vai para a tela de login
        sm.current = "login"

    def on_enter(self, *args):
        # Carrega os dados do usuário ao entrar na tela
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    # Cria um popup para login inválido
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    # Cria um popup para formulário inválido
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


# Carrega o arquivo KV
kv = Builder.load_file("my.kv")

# Cria o gerenciador de telas e o banco de dados
sm = WindowManager()
db = DataBase("users.txt")

# Adiciona as telas ao gerenciador
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"  # Define a tela inicial


class MyMainApp(App):
    def build(self):
        return sm  # Retorna o gerenciador de telas


# Executa o aplicativo
if __name__ == "__main__":
    MyMainApp().run()
