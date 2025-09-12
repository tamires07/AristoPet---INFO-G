from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    email = models.EmailField(unique=True, verbose_name="Email")
    senha = models.CharField(unique=True, max_length=100, verbose_name="Senha")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    def __str__(self):
        return f"{self.nome}, {self.data_nasc}, {self.endereco}, {self.email}, {self.senha}, {self.telefone}"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    email = models.EmailField(verbose_name="Email")
    senha = models.CharField(max_length=100, verbose_name="Senha")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    def __str__(self):
        return f"{self.nome}, {self.cnpj}, {self.endereco}, {self.email}, {self.senha}, {self.telefone}"

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Animal(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Animal")
    especie = models.CharField(max_length=50, verbose_name="Espécie")
    genero = models.CharField(max_length=50, verbose_name="Gênero")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    doador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Doador")

    def __str__(self):
        return f"{self.nome}, {self.especie}, {self.genero}, {self.cidade}, Doador: {self.doador}"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

class Adocao(models.Model):
    doador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Doador")
    adotante = models.ForeignKey(Pessoa, related_name='adotante', on_delete=models.CASCADE, verbose_name="Adotante")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    data_adocao = models.DateField(auto_now_add=True, verbose_name="Data de Adoção")

    def __str__(self):
        return f"{self.doador}, {self.adotante},{self.animal}, {self.data_adocao}"

    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"

class Evento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Evento")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    data_hora = models.DateTimeField(verbose_name="Data e Hora do Evento")
    local = models.CharField(max_length=200, verbose_name="Local do Evento")
    descricao = models.TextField(verbose_name="Descrição do Evento")

    def __str__(self):
        return f"{self.nome}, {self.instituicao}, {self.data_hora}, {self.local}, {self.descricao}"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"