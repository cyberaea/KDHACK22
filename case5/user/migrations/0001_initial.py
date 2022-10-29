# Generated by Django 4.1.2 on 2022-10-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('hall', models.IntegerField()),
                ('hardware', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]