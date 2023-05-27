from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from apps.convenios.models import Convenio
from apps.especialidades.models import Especialidade
from apps.setores.models import Setor
from django_cpf_cnpj.fields import CPFField

class Pessoa(models.Model):
    SEXO = (
        ("MAS", "Maculino"),
        ("FEM", "Feminino")
    )
    GRUPO_SANGUINEO = (
        ("TIPO A+", "A+"),
        ("TIPO B+", "B+"),
        ("TIPO O+", "O+"),
        ("TIPO AB+", "AB+"),
        ("TIPO A-", "A-"),
        ("TIPO B-", "B-"),
        ("TIPO O-", "O-"),
        ("TIPO AB-", "AB-")
    )
    nome = models.CharField(verbose_name="Nome", max_length=45)
    crm = models.CharField(verbose_name="CRM", max_length=45, null=True, blank=True)
    data_cadastro = models.DateField(null=True)
    data_nascimento = models.DateField(null=True)
    sexo = models.CharField(verbose_name="Sexo", max_length=45, choices=SEXO, null=True, blank=True)
    grupo_sanguineo = models.CharField(verbose_name="Grupo Sanguineo", max_length=45, choices=GRUPO_SANGUINEO, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número precisa estar neste formato: \
                            '+99 99 99999-0000'.")
    telefone = models.CharField(verbose_name="Telefone", max_length=45, validators=[phone_regex], null=True)
    nome_mae = models.CharField(verbose_name="Nome da Mãe", max_length=45, null=True)
    nome_pai = models.CharField(verbose_name="Nome do Pai", max_length=45, null=True, blank=True)
    cpf = CPFField(verbose_name="CPF", max_length=14, null=True, unique=True)
    rg = models.CharField(verbose_name="RG", max_length=45, null=True, blank=True, unique=True)
    registro_atualizado = models.DateTimeField()
    registro_criado = models.DateTimeField()
    pessoa = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, null=True, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, related_name="pessoas", null=True, blank=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.PROTECT, related_name="pessoas", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'pessoa'