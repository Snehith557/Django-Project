# Generated by Django 4.2.4 on 2023-09-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedBacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]