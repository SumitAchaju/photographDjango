# Generated by Django 4.1.2 on 2022-11-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CategoryImage')),
                ('discription', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
