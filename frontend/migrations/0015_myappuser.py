# Generated by Django 2.0 on 2021-01-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_auto_20210127_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyAppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=135)),
            ],
        ),
    ]
