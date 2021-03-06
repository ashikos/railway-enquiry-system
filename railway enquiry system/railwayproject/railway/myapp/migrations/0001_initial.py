# Generated by Django 4.0.1 on 2022-03-04 15:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('contact_no', models.IntegerField()),
                ('c_from', models.CharField(max_length=300)),
                ('c_to', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=500)),
                ('passenger', models.IntegerField()),
                ('payement', models.IntegerField()),
                ('ac_no', models.IntegerField()),
                ('ex_date', models.DateField()),
                ('cvv', models.IntegerField()),
                ('holder', models.CharField(max_length=300)),
                ('uname', models.CharField(default='None', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.CharField(max_length=300)),
                ('firstName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('contact_no', models.IntegerField()),
                ('c_from', models.CharField(max_length=300)),
                ('c_to', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('passenger', models.IntegerField()),
                ('uname', models.CharField(default='None', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='train_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.CharField(max_length=300)),
                ('d_place', models.CharField(max_length=300)),
                ('a_place', models.CharField(max_length=300)),
                ('d_time', models.TimeField(max_length=300)),
                ('a_time', models.TimeField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=300)),
                ('fname', models.CharField(max_length=300)),
                ('lname', models.CharField(max_length=300)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
