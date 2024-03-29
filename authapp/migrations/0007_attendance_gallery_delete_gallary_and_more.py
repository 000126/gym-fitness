# Generated by Django 4.2 on 2023-10-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_gallary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selectdate', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.CharField(max_length=15)),
                ('Login', models.CharField(max_length=200)),
                ('Logout', models.CharField(max_length=200)),
                ('SelectWorkout', models.CharField(max_length=200)),
                ('TrainedBy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.DeleteModel(
            name='Gallary',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='Referance',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='price',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='DueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='FullName',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Gender',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='PhoneNumber',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='SelectMembershipplan',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='SelectTrainer',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='paymentStatus',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='plan',
            field=models.CharField(max_length=185),
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(max_length=55),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='phone',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.IntegerField(max_length=25),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, max_length=55, null=True),
        ),
    ]
