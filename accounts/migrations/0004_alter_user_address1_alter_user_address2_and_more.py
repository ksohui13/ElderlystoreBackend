# Generated by Django 4.2.3 on 2023-08-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_active_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address1',
            field=models.CharField(default='address1', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.CharField(default='address2', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='address3',
            field=models.CharField(default='address3', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password1',
            field=models.CharField(default='password1', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(default='password2', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
