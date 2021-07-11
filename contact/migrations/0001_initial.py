# Generated by Django 3.2.4 on 2021-07-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=90)),
                ('subject', models.TextField()),
                ('date', models.CharField(default='', max_length=12)),
                ('time', models.CharField(default='', max_length=12)),
                ('message', models.TextField()),
            ],
        ),
    ]