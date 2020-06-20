from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#1 Логирование
class Log(models.Model):
    create_duid = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Наименование', max_length=300, default=None, blank=True, null=True)
    log_data = models.CharField(verbose_name='Информация', max_length=20000, default=None, blank=True, null=True)

#2 Департамент, подразделение
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    depart_name = models.CharField(verbose_name='Название департамента', max_length=200, default=None, blank=True, null=True)

#3 Отдел
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(verbose_name='Название отдела', max_length=500, default=None, blank=True, null=True)
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="id")

#4 пользователи организации
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(verbose_name='ФИО', max_length=100, default=None, blank=True, null=True)
    position = models.CharField(verbose_name='Должность', max_length=200, default=None, blank=True, null=True)
    mail = models.CharField(verbose_name='Е-мейл', max_length=50, default=None, blank=True, null=True)
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="id")
    group_name =  models.ForeignKey(Group, on_delete=models.CASCADE, related_name="id")


#5 пользователь (личный кабинет)
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(verbose_name="Аватар")
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="user")
    position = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="position")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    group =  models.ForeignKey(Group, on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='Телефон', max_length=20, default=None, blank=True, null=True)
    mail = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="mail")
    rating = models.IntegerField(verbose_name='Рейтинг', max_length=10, default=None, blank=True, null=True)
    password = models.CharField(verbose_name="Пароль", max_length=50, default=None, blank=True, null=True)
    date_birth = models.DateTimeField(verbose_name="Дата рождения")
    sex = models.CharField(verbose_name="Пол", max_length=1, default=None, blank=True, null=True)



#6 Атрибут идеи (свойства)
class OfferAttr(models.Model):
    id = models.AutoField(primary_key=True)
    prior_val =  models.IntegerField(verbose_name="Приоритет", max_length=1, default=None, blank=True, null=True)
     

#7 Идея (справочник)
class Offer(models.Model):]
    id = models.AutoField(primary_key=True)
    offer_type_name = models.CharField(verbose_name="Наименование (тип)", max_length=100, default=None, blank=True, null=True)
    detail = models.CharField(verbose_name="Описание", max_length=1000, default=None, blank=True, null=True)
    avatar = models.ImageField(verbose_name="Аватар")
    status = models.IntegerField(verbose_name="Статус", max_length=1, default=None, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    create_duid = models.DateTimeField(auto_now_add=True)
    prior = models.ForeignKey(OfferAttr, on_delete=models.PROTECT)

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
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    prior = models.ForeignKey(OfferAttr, on_delete=models.PROTECT)
    vote_posit =  models.IntegerField(verbose_name="Голосование за", max_length=1, default=None, blank=True, null=True)
    vote_negat = models.IntegerField(verbose_name="Голосование против", max_length=1, default=None, blank=True, null=True)
    create_duid = models.DateTimeField(auto_now_add=True)

#10 Закладки
class OfferFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    user =  models.ForeignKey(Person, on_delete=models.CASCADE)
    offer_run =  models.ForeignKey(OfferRun, on_delete=models.CASCADE)


#11 коммент к идеи
class OfferComment(models.Model):
    id = models.AutoField(primary_key=True)
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    text = models.CharField(verbose_name='Информация', max_length=20000, default=None, blank=True, null=True)
    like =  models.IntegerField(verbose_name="Лайк", max_length=1, default=None, blank=True, null=True)
    create_duid = models.DateTimeField(auto_now_add=True)


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
