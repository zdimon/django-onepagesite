# Generated by Django 2.2.4 on 2019-10-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_page_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='on_main',
            field=models.BooleanField(default=False),
        ),
    ]
