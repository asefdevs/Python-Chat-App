# Generated by Django 5.0 on 2024-01-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
