# Generated by Django 3.1.1 on 2020-09-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=100)),
                ('lname', models.CharField(default='', max_length=100)),
                ('procedure', models.CharField(choices=[('S', 'SURGERY'), ('C', 'CLEANING THE FACE'), ('M', 'MEZOPIYA')], default='', max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]