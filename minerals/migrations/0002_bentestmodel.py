# Generated by Django 2.2.6 on 2019-12-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('test_filename', models.CharField(max_length=255)),
            ],
        ),
    ]
