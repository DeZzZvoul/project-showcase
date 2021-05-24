from django.db import models
from django.urls import reverse
class Users(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    e_mail = models.EmailField(max_length=45, null=False, unique=True)
    phone_num = models.CharField(max_length=12)
    vk_link = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Problems(models.Model):
    title = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=1000, null=False)
    owner = models.ForeignKey('Users',on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.title

class Projects(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=90, null=False, verbose_name='Название проекта')
    imprint = models.ImageField()
    shortdescription = models.CharField(max_length=500, null=False, verbose_name='Краткое описание')
    description = models.CharField(max_length=2000, null=False, verbose_name='Описание')
    problem = models.CharField(max_length=2000, null=False, verbose_name= 'Проблема')
    analysis = models.CharField(max_length=2000, null=False, verbose_name='Ситуация')
    curator = models.CharField(max_length=45, verbose_name='Куратор')
    project = models.ManyToManyField('Users', related_name='project', verbose_name='Руководитель проекта')

    def get_absolute_url(self):
        return reverse('project_page', kwargs={'pr_id': self.id})

    def __str__(self):
        return self.title