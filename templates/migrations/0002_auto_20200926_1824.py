# Generated by Django 3.0.5 on 2020-09-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='data_type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='default',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_type_label',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='is_removable',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='label',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='field',
            name='mandatory',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='customerId',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='entity',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='template',
            name='law',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
