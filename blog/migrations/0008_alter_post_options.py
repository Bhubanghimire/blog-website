# Generated by Django 3.2.4 on 2021-06-19 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('order',)},
        ),
    ]