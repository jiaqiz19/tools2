# Generated by Django 2.2.7 on 2019-11-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of pet', max_length=100)),
                ('species', models.CharField(help_text='Species of animals', max_length=50)),
                ('birth_date', models.DateField(help_text='Birth Date')),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', help_text='Sex of pet', max_length=16)),
            ],
        ),
    ]
