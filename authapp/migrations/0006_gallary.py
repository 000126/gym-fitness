# Generated by Django 4.2 on 2023-10-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_enrollment_duedate_enrollment_paymentstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pics', models.ImageField(upload_to='gallary')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
