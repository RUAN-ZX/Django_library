# Generated by Django 3.0.2 on 2020-03-06 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200228_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('图书管理员权限', 'Set book as returned'),)},
        ),
    ]
