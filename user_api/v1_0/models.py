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
    depart_name = models.CharField(verbose_name='Название департамента', max_length=200, default=None, blank=True, null=True)

#3 Отдел
class Group(models.Model):
    group_name = models.CharField(verbose_name='Название отдела', max_length=500, default=None, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

#4 пользователи организации
# class Users(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.CharField(verbose_name='ФИО', max_length=100, default=None, blank=True, null=True)
#     position = models.CharField(verbose_name='Должность', max_length=200, default=None, blank=True, null=True)
#     mail = models.CharField(verbose_name='Е-мейл', max_length=50, default=None, blank=True, null=True)
#     depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="id")
#     group_name =  models.ForeignKey(Group, on_delete=models.CASCADE, related_name="id")


#5 пользователь (личный кабинет)
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(verbose_name="Аватар")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
#    position = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="position")
    position = models.CharField(verbose_name='Должность', max_length=200, default=None, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    group =  models.ForeignKey(Group, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Телефон', max_length=20, default=None, blank=True, null=True)
#    mail = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="mail")
    mail = models.CharField(verbose_name='Е-мейл', max_length=50, default=None, blank=True, null=True)
    rating = models.IntegerField(verbose_name='Рейтинг', default=None, blank=True, null=True)
    password = models.CharField(verbose_name="Пароль", max_length=50, default=None, blank=True, null=True)
    date_birth = models.DateTimeField(verbose_name="Дата рождения")
    sex = models.CharField(verbose_name="Пол", max_length=1, default=None, blank=True, null=True)

