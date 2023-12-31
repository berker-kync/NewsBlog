# Generated by Django 4.2.4 on 2023-09-09 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_modified_remove_comment_news_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.news'),
        ),
        migrations.AddField(
            model_name='comment',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
