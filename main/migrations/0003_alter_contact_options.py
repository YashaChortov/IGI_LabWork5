# Generated by Django 4.2.22 on 2025-06-10 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact_faq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
    ]
