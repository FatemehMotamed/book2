# Generated by Django 3.0.2 on 2020-08-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='home.Author'),
        ),
    ]
