# Generated by Django 3.2.4 on 2021-06-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.DateTimeField(auto_now=True),
        ),
    ]