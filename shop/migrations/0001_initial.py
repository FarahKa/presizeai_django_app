# Generated by Django 3.2.8 on 2021-10-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizeid', models.CharField(max_length=6)),
                ('last_activity', models.DateField()),
            ],
        ),
    ]
