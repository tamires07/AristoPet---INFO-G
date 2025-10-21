from django.db import models

class Caracteristica_Objetivo(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso")
    altura = models.IntegerField(verbose_name="Altura(centímetros)")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    genero = models.CharField(max_length=15, verbose_name="Gênero")
    nivel_atividade = models.CharField(max_length=10, verbose_name="Nível de atividade")
    objetivo = models.CharField(max_length=50, verbose_name="Objetivo")
    detalhamento = models.CharField(max_length=100, verbose_name="Detalhamento")

    def __str__(self):
        return f"{self.peso}, {self.altura}, {self.data_nasc}, {self.genero}, {self.nivel_atividade}, {self.objetivo}, {self.detalhamento}"
    class Meta:
        verbose_name = "Caracteristica_Objetivo"
        verbose_name_plural = "Caracteristicas_Objetivos"

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.CharField(max_length=50, verbose_name="Email")
    senha = models.CharField(max_length=50, verbose_name="Senha")
    telefone = models.CharField(max_length=50, verbose_name="Telefone")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    nome_perfil = models.CharField(max_length=50, verbose_name="Nome de perfil")
    Caracteristica_Objetivo = models.ForeignKey(Caracteristica_Objetivo, on_delete=models.CASCADE, verbose_name="Características e objetivo")
    recado = models.CharField(max_length=50, verbose_name="Deixe um recado")

    def __str__(self):
        return f"{self.nome}, {self.email}, {self.senha}, {self.telefone}, {self.endereco}, {self.nome_perfil}, {self.Caracteristica_Objetivo}, {self.recado}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Agenda(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    data_hora = models.DateTimeField(verbose_name="Data e hora")

    def __str__(self):
        return f"{self.nome}, {self.data_hora}"
    
    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

class Evento(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    data_hora = models.DateTimeField(verbose_name="Data e hora")
    local = models.CharField(max_length=100, verbose_name="Local")
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome}, {self.data_hora}, {self.local}, {self.descricao}"
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Lembrete(models.Model):
    Agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name="nome")
    cor = models.CharField(max_length=50, verbose_name="Cor")
    som = models.CharField(max_length=50, verbose_name="Som")

    def __str__(self):
        return f"{self.Agenda}, {self.cor}, {self.som}"
    
    class Meta:
        verbose_name = "Lembrete"
        verbose_name_plural = "Lembretes"

class Dieta_Objetivo(models.Model):
    Caracteristica_Objetivo = models.ForeignKey(Caracteristica_Objetivo, on_delete=models.CASCADE, verbose_name="Característica e objetivo")
    dite_tipo = models.CharField(max_length=150, verbose_name="Tipo de dieta")

    def __str__(self):
        return f"{self.Caracteristica_Objetivo}, {self.dite_tipo}"
    
    class Meta:
        verbose_name = "Dieta_Objetivo"
        verbose_name_plural = "Dietas_Objetivos"

class Plano_Atividade(models.Model):
    Caracteristica_Objetivo = models.ForeignKey(Caracteristica_Objetivo, on_delete=models.CASCADE, verbose_name="Característica e objetivo")
    treino_ideal = models.CharField(max_length=150, verbose_name="Treino ideal")

    def __str__(self):
        return f"{self.Caracteristica_Objetivo}, {self.treino_ideal}"
    
    class Meta:
        verbose_name = "Plano_Atividade"
        verbose_name_plural = "Planos_Atividades"

class Exercicio(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do exercício")
    dificuldade = models.CharField(max_length=15, verbose_name="Dificuldade")
    descricao = models.CharField(max_length=150, verbose_name="Descrição do exercício")

    def __str__(self):
        return f"{self.nome}, {self.dificuldade}, {self.descricao}"
    
    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"

class Filtrar_Atividade(models.Model):
    Caracteristica_Objetivo = models.ForeignKey(Caracteristica_Objetivo, on_delete=models.CASCADE, verbose_name="Característica e objetivo")
    dificuldade = models.CharField(max_length=15, verbose_name="Dificuldade")
    tipo = models.CharField(max_length=150, verbose_name="Tipo")

    def __str__(self):
        return f"{self.Caracteristica_Objetivo}, {self.dificuldade}, {self.tipo}"
    
    class Meta:
        verbose_name = "Filtrar_Atividade"
        verbose_name_plural = "Filtrar_Atividades"

class Experiencia(models.Model):
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return f"{self.descricao}"
    
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

class Progresso(models.Model):
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    cal_consumida = models.IntegerField(verbose_name="Calorias consumidas no dia (kcal)")
    cal_gasta = models.IntegerField(verbose_name="Calorias gastas no dia (kcal)")
    proteina = models.IntegerField(verbose_name="Proteinas consumidas no dia (g)")
    gordura = models.IntegerField(verbose_name="Gorduras consumidas no dia (g)")
    peso_perdido = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso Perdido no total(kg)")
    peso_ganho = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso ganho no total(kg)")

    def __str__(self):
            return f"{self.Pessoa}, {self.cal_consumida}, {self.cal_gasta}, {self.proteina}, {self.gordura}, {self.peso_perdido}, {self.peso_ganho}"
    
    class Meta:
        verbose_name = "Progresso"
        verbose_name_plural = "Progressos"

class Feedback(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return f"{self.descricao}"
    
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
