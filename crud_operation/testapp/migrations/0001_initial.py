# Generated by Django 3.2.4 on 2021-06-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=3)),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
