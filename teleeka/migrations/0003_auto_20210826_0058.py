# Generated by Django 3.2.6 on 2021-08-26 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleeka', '0002_auto_20210826_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='amount_to_deposit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='withdrwal',
            name='amount_to_deposit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='withdrwal',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
