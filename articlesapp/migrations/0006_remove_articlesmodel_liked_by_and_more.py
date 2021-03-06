# Generated by Django 4.0.4 on 2022-05-04 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articlesapp', '0005_articlesmodel_liked_by_alter_articlesmodel_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesmodel',
            name='liked_by',
        ),
        migrations.AlterField(
            model_name='articlesmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='articlesmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myarticles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ArticlesRelationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=600)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articlesapp.articlesmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
