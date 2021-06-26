# Generated by Django 3.2.3 on 2021-06-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('UT', 'UTILITY'), ('PL', 'PLANTS')], default='UT', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
