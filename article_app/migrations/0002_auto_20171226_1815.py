# Generated by Django 2.0 on 2017-12-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='article_app.Category', verbose_name='related category'),
        ),
    ]
