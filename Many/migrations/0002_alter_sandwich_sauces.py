# Generated by Django 3.2.6 on 2021-10-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Many', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='sauces',
            field=models.ManyToManyField(related_name='sandwiches', to='Many.Sauce'),
        ),
    ]