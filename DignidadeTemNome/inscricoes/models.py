from django.db import models
from datetime import date

class Inscricao(models.Model):
    RENDA_CHOICES = [
        ('<1', 'menos de um salário mínimo'),
        ('1', 'até um salário mínimo'),
        ('2-3', 'de dois a três salários mínimos'),
        ('3-4', 'de três a quatro salários mínimos'),
        ('4-5', 'de quatro a cinco salários mínimos'),
        ('>5', 'mais de cinco salários mínimos'),
    ]

    ETNIA_CHOICES = [
        ('negra', 'Negra'),
        ('indigena', 'Indígena'),
        ('cigana', 'Cigana'),
        ('quilombola', 'Quilombola'),
        ('parda', 'Parda'),
        ('branca', 'Branca'),
        ('amarela', 'Amarela'),
    ]

    TERRITORIO_CHOICES = [
        ('metropolitana', 'Território Região Metropolitana de Natal'),
        ('agreste', 'Território Agreste / Litoral Sul'),
        ('mato_grande', 'Território Mato Grande'),
        ('potengi', 'Território Potengi'),
        ('trairi', 'Território Trairí'),
        ('sertao_central', 'Território Sertão Central Cabugi / Litoral Norte'),
        ('serido', 'Território Seridó'),
        ('assu_mossoro', 'Território Assú / Mossoró'),
        ('apodi', 'Território Sertão do Apodi'),
        ('alto_oeste', 'Território Alto Oeste'),
    ]

    GENERO_CHOICES = [
        ('travesti', 'Travesti'),
        ('mulher_transexual', 'Mulher Transexual'),
        ('homem_transexual', 'Homem Transexual'),
        ('intersexual', 'Intersexual'),
        ('nao_binario', 'Não Binárie'),
        ('trans_masculine', 'Trans Masculine'),
        ('outro', 'Outro'),
    ]

    nome_civil = models.CharField(max_length=200)
    nome_social = models.CharField(max_length=200, blank=True)
    rg_numero = models.CharField(max_length=50)
    rg_orgao_expedidor = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    renda_familiar = models.CharField(max_length=10, choices=RENDA_CHOICES)
    territorio = models.CharField(max_length=50, choices=TERRITORIO_CHOICES)
    telefone = models.CharField(max_length=20)
    genero_sexualidade = models.CharField(max_length=50, choices=GENERO_CHOICES)
    etnia = models.CharField(max_length=20, choices=ETNIA_CHOICES)
    populacao_de_rua = models.BooleanField(default=False)
    rg_anexo = models.FileField(upload_to='documentos/')

    pontuacao = models.FloatField(default=0)

    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def calcular_pontuacao(self):
        idade = self.calcular_idade()
        idade_peso = 1 + idade / 100
        renda_peso = {
            '<1': 1.5,
            '1': 1.4,
            '2-3': 1.3,
            '3-4': 1.2,
            '4-5': 1.1,
            '>5': 1.0
        }.get(self.renda_familiar, 1.0)
        etnia_peso = {
            'negra': 1.4,
            'indigena': 1.4,
            'cigana': 1.4,
            'quilombola': 1.4,
            'parda': 1.2,
            'branca': 1.0,
            'amarela': 1.0
        }.get(self.etnia, 1.0)
        rua_peso = 1.5 if self.populacao_de_rua else 1.0
        self.pontuacao = round(10 * idade_peso * renda_peso * etnia_peso * rua_peso, 2)

    def save(self, *args, **kwargs):
        self.calcular_pontuacao()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_civil
