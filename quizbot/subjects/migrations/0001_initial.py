# Generated by Django 4.0 on 2022-12-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.TextField()),
                ('op2', models.TextField()),
                ('op3', models.TextField()),
                ('op4', models.TextField()),
            ],
        ),
    ]