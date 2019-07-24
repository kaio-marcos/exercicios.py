class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_idade(self, idade):
        self.idade = idade

class Pet(Pessoa):
    def __init__(self, nome, idade, nome_animal, data_nascimento):
        super().__init__(nome, idade)
        self.nome_animal = nome_animal
        self.data_nascimento = data_nascimento

    def get_nome_animal(self):
        return self.nome_animal

    def get_data_nascimento(self):
        return self.data_nascimento
    
    def set_nome_animal(self, nome_animal):
        self.nome_animal = nome_animal

    def set_idade(self, data_nascimento):
        self.data_nascimento = data_nascimento

    #def get_nome_dono(self):
    #   return super().get_nome()

dados = Pessoa('vai_ser_alterado', 18)
animal = Pet(dados.get_nome(), dados.get_idade(), 'vai alterar', 23)
#dog = Pet('kakalkdash', 2019)

#dog.get_idade(input('campeão, digite a data, mes e ano de nascimento do seu pet'))
animal.set_nome_animal(input('Qual o nome do seu animal: '))
dados.set_nome(input('Qual seu nome cachorro loko?: ' ))
dados.set_idade(input('fala sua idade ae pá nois: ' ))

#print(f'{dog.get_nome} {dog.get_data_nascimento}')
print(f'Nome: {dados.get_nome()} || Idade: {dados.get_idade()} anos')
print(f'o nome do seu animal é {animal.get_nome_animal}' )

#animal = Pet('obede', 18, 'costela', 2019)
#print(f'{animal.get_nome()} nascido em: {animal.get_data_nascimento()}')