# Generated by Django 2.0.6 on 2018-08-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0031_auto_20180828_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Image',
            field=models.ImageField(blank=True, default='..static/img/noimage.PNG', null=True, upload_to='mypics/%Y/%m/%d'),
        ),
    ]
