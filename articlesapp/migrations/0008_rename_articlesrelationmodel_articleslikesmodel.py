# Generated by Django 4.0.4 on 2022-05-04 11:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articlesapp', '0007_remove_articlesrelationmodel_comment_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticlesRelationModel',
            new_name='ArticlesLikesModel',
        ),
    ]
