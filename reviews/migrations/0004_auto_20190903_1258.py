# Generated by Django 2.2.4 on 2019-09-03 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190903_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='username',
            new_name='user',
        ),
    ]
