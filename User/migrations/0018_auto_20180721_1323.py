# Generated by Django 2.0.6 on 2018-07-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0017_auto_20180721_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Image',
            field=models.ImageField(blank='True', default='mypics/noimage.png', null='True', upload_to='mypics/%Y/%m/%d'),
        ),
    ]
