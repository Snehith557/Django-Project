# Generated by Django 4.2.4 on 2023-09-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedbacks_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]