# Generated by Django 4.0 on 2021-12-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('salary', models.PositiveSmallIntegerField()),
                ('prefectures', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
