# Generated by Django 3.1.7 on 2021-03-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megahack2', '0002_auto_20210310_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='mobile_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='email_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/speaker'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='instagram_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='linkedIn_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='sub_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
