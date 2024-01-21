# Generated by Django 4.2.7 on 2024-01-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text_color', models.CharField(max_length=100)),
                ('background_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('categories', models.ManyToManyField(to='blog.category')),
            ],
        ),
    ]