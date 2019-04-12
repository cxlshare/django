# Generated by Django 2.2 on 2019-04-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=64)),
                ('product_description', models.TextField(max_length=256)),
                ('purchase_date', models.DateField()),
            ],
        ),
    ]