from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Log(models.Model):
    create_duid = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Наименование', max_length=300, default=None, blank=True, null=True)
    log_data = models.CharField(verbose_name='Информация', max_length=20000, default=None, blank=True, null=True)

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="Аватар")
    deartment = models.CharField(verbose_name='Отдел', max_length=200, default=None, blank=True, null=True)
    position = models.CharField(verbose_name='Должность', max_length=200, default=None, blank=True, null=True)

class Offer(models.Model):
    offer_name = models.CharField(verbose_name="Наименование", max_length=1000, default=None, blank=True, null=True)
    detail = models.CharField(verbose_name="Срок договора", max_length=100, default=None, blank=True, null=True)
    avatar = models.ImageField(verbose_name="Аватар")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    create_duid = models.DateTimeField(auto_now_add=True)

class OfferTag(models.Model):
    tag_name  = models.CharField(verbose_name="Наименование", max_length=100, default=None, blank=True, null=True)
    tag_value = models.CharField(verbose_name="Значение", max_length=100, default=None, blank=True, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

class OfferComment(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Информация', max_length=20000, default=None, blank=True, null=True)



# class Agent(models.Model):
#     fname = models.CharField(verbose_name="ФИО", max_length=1000, default=None, blank=True, null=True)
#     dogdate = models.DateTimeField(verbose_name="Дата договора",default=None, blank=True, null=True)
#     dogdue = models.CharField(verbose_name="Срок договора", max_length=100, default=None, blank=True, null=True)
#     inn = models.CharField(verbose_name="ИНН", max_length=100, default=None, blank=True, null=True)
#     site = models.URLField(verbose_name="Веб-сайт", default=None, blank=True, null=True)
#     atype = models.CharField(verbose_name="Тип агента", max_length=10, default=None, blank=True, null=True)

# class AgentKind(models.Model):
#     agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
#     kind = models.CharField(verbose_name="Вид страхования", max_length=5000, default=None, blank=True, null=True)
