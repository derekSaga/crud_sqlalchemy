class ClienteDto:
    def __init__(self, nome, email, senha, dt_nascimento):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__dt_nascimento = dt_nascimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def dt_nascimento(self):
        return self.__dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, dt_nascimento):
        self.__dt_nascimento = dt_nascimento
