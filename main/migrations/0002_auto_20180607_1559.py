# Generated by Django 2.0.6 on 2018-06-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='header',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_code',
            field=models.CharField(default='4NshVUr5HRx3TTqpgknf', max_length=20),
        ),
    ]