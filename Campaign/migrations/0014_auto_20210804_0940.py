# Generated by Django 3.2.6 on 2021-08-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0013_auto_20200601_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='campaigndata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='campaignteam',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='trusteduser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]