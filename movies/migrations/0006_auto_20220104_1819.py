# Generated by Django 3.2.7 on 2022-01-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20211225_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newmovie',
            name='Poster',
            field=models.ImageField(upload_to='media/movies/%y/%m/'),
        ),
        migrations.AlterField(
            model_name='newmovie',
            name='Sample1',
            field=models.ImageField(upload_to='media/sample1/%y/%m/'),
        ),
        migrations.AlterField(
            model_name='newmovie',
            name='Sample2',
            field=models.ImageField(upload_to='media/sample2/%y/%m/'),
        ),
        migrations.AlterField(
            model_name='newmovie',
            name='Sample3',
            field=models.ImageField(upload_to='media/sample3/%y/%m/'),
        ),
    ]
