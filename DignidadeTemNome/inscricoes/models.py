from django.db import models

class Inscricao(models.Model):
    RENDA_CHOICES = [
        ('menos_de_um', 'Menos de um salário mínimo'),
        ('ate_um', 'Até um salário mínimo'),
        ('dois_a_tres', 'De dois a três salários mínimos'),
        ('tres_a_quatro', 'De três a quatro salários mínimos'),
        ('quatro_a_cinco', 'De quatro a cinco salários mínimos'),
        ('outro', 'Outro'),
    ]

    TERRITORIO_CHOICES = [
        ('rmn', 'Região Metropolitana de Natal'),
        ('agreste', 'Agreste / Litoral Sul'),
        ('mato_grande', 'Mato Grande'),
        ('potengi', 'Potengi'),
        ('trairi', 'Trairí'),
        ('sertao_cabugi', 'Sertão Central Cabugi / Litoral Norte'),
        ('serido', 'Seridó'),
        ('assu_mossoro', 'Assú / Mossoró'),
        ('sertao_apodi', 'Sertão do Apodi'),
        ('alto_oeste', 'Alto Oeste'),
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

    ETNIA_CHOICES = [
        ('negra', 'Negra'),
        ('indigena', 'Indígena'),
        ('cigana', 'Cigana'),
        ('quilombola', 'Quilombola'),
        ('parda', 'Parda'),
        ('branca', 'Branca'),
        ('amarela', 'Amarela'),
    ]

    renda_familiar = models.CharField(max_length=20, choices=RENDA_CHOICES)
    nome_civil = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    rg_numero = models.CharField(max_length=20)
    rg_orgao_expedidor = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    rg_anexo = models.FileField(upload_to='uploads/rg/')
    territorio = models.CharField(max_length=30, choices=TERRITORIO_CHOICES)
    telefone = models.CharField(max_length=20)
    genero_sexualidade = models.CharField(max_length=30, choices=GENERO_CHOICES)
    etnia = models.CharField(max_length=20, choices=ETNIA_CHOICES)

    def __str__(self):
        return self.nome_civil
