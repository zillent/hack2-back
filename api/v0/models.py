from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#1 Логирование
class Log(models.Model):
    create_duid = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Наименование', max_length=300, default=None, blank=True, null=True)
    log_data = models.CharField(verbose_name='Информация', max_length=20000, default=None, blank=True, null=True)

#6 Атрибут идеи (свойства)
class OfferAttr(models.Model):
    id = models.AutoField(primary_key=True)
    prior_val =  models.IntegerField(verbose_name="Приоритет", default=None, blank=True, null=True)
     

#7 Идея (справочник)
class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    offer_type_name = models.CharField(verbose_name="Наименование (тип)", max_length=100, default=None, blank=True, null=True)
    detail = models.CharField(verbose_name="Описание", max_length=1000, default=None, blank=True, null=True)
    avatar = models.ImageField(verbose_name="Аватар", default=None, blank=True, null=True)
    status = models.IntegerField(verbose_name="Статус", default=None, blank=True, null=True)
    person_id = models.IntegerField(verbose_name="ИД пользователя", default=None, blank=True, null=True)
    create_duid = models.DateTimeField(auto_now_add=True)
    prior = models.ForeignKey(OfferAttr, on_delete=models.PROTECT, default=None, blank=True, null=True)

#8 Теги идеи
class OfferTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name  = models.CharField(verbose_name="Наименование", max_length=100, default=None, blank=True, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

#9 Запущенные идеи (объект создан)
class OfferRun(models.Model):
    id = models.AutoField(primary_key=True)
    type_offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    head = models.CharField(verbose_name="Заголовок", max_length=100, default=None, blank=True, null=True)
    detail = models.CharField(verbose_name="Текст идеи", max_length=10000, default=None, blank=True, null=True)
    attach = models.ImageField(verbose_name="Вложение") # TODO для  всех типов
    tags =  models.ForeignKey(OfferTag, on_delete=models.PROTECT)
    group_id = models.IntegerField(verbose_name="ИД группы", default=None, blank=True, null=True)
    prior = models.ForeignKey(OfferAttr, on_delete=models.PROTECT)
    vote_posit =  models.IntegerField(verbose_name="Голосование за", default=None, blank=True, null=True)
    vote_negat = models.IntegerField(verbose_name="Голосование против", default=None, blank=True, null=True)
    create_duid = models.DateTimeField(auto_now_add=True)

#10 Закладки
class OfferFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    person_id =  models.IntegerField(verbose_name="ИД пользователя", default=None, blank=True, null=True)
    offer_run =  models.ForeignKey(OfferRun, on_delete=models.CASCADE)


#11 коммент к идеи
class OfferComment(models.Model):
    id = models.AutoField(primary_key=True)
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT)
    person_id =  models.IntegerField(verbose_name="ИД пользователя", default=None, blank=True, null=True)
    text = models.CharField(verbose_name='Информация', max_length=20000, default=None, blank=True, null=True)
    like =  models.IntegerField(verbose_name="Лайк", default=None, blank=True, null=True)
    create_duid = models.DateTimeField(auto_now_add=True)

