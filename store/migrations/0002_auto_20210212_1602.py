# Generated by Django 3.1.6 on 2021-02-12 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='designation',
            new_name='description',
        ),
    ]
