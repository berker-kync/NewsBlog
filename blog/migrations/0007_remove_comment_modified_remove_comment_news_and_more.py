# Generated by Django 4.2.4 on 2023-09-09 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='published',
        ),
    ]