# Generated by Django 3.2.5 on 2021-07-31 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asks', '0002_rename_post_ask_hospital'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ask',
            options={'ordering': ('created',)},
        ),
    ]