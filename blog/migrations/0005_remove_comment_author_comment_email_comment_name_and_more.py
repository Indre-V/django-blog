# Generated by Django 4.2.11 on 2024-04-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
