# Generated by Django 4.1.5 on 2023-01-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_receivers_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Insta_password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Insta_receiver',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Insta_username',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Receivers_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Receivers_phone_no',
            field=models.IntegerField(null=True),
        ),
    ]
