# Generated by Django 5.1.1 on 2024-09-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('time', models.DateField(auto_now_add=True)),
                ('feelings', models.TextField()),
                ('mood_intensity', models.IntegerField()),
            ],
        ),
    ]
