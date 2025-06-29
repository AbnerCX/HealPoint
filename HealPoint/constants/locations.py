from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Nationalities(IntegerChoices):
    MEXICAN = 1, _("Mexican")
    FOREIGN = 2, _("Foreign")


class Countries(IntegerChoices):
    MEXICO = 1, _("Mexico")
    OTHER = 99, _("Other")


class MexicanStates(IntegerChoices):
    AGUASCALIENTES = 1, _("Aguascalientes")
    BAJA_CALIFORNIA = 2, _("Baja California")
    BAJA_CALIFORNIA_SUR = 3, _("Baja California Sur")
    CAMPECHE = 4, _("Campeche")
    CHIAPAS = 5, _("Chiapas")
    CHIHUAHUA = 6, _("Chihuahua")
    CIUDAD_DE_MEXICO = 7, _("Ciudad de México")
    COAHUILA = 8, _("Coahuila")
    COLIMA = 9, _("Colima")
    DURANGO = 10, _("Durango")
    ESTADO_MEXICO = 11, _("Estado de México")
    GUANAJUATO = 12, _("Guanajuato")
    GUERRERO = 13, _("Guerrero")
    HIDALGO = 14, _("Hidalgo")
    JALISCO = 15, _("Jalisco")
    MICHOACAN = 16, _("Michoacán")
    MORELOS = 17, _("Morelos")
    NAYARIT = 18, _("Nayarit")
    NUEVO_LEON = 19, _("Nuevo León")
    OAXACA = 20, _("Oaxaca")
    PUEBLA = 21, _("Puebla")
    QUERETARO = 22, _("Querétaro")
    QUINTANA_ROO = 23, _("Quintana Roo")
    SAN_LUIS_POTOSI = 24, _("San Luis Potosí")
    SINALOA = 25, _("Sinaloa")
    SONORA = 26, _("Sonora")
    TABASCO = 27, _("Tabasco")
    TAMAULIPAS = 28, _("Tamaulipas")
    TLAXCALA = 29, _("Tlaxcala")
    VERACRUZ = 30, _("Veracruz")
    YUCATAN = 31, _("Yucatán")
    ZACATECAS = 32, _("Zacatecas")