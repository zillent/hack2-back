# Generated by Django 3.0.4 on 2020-06-20 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0003_auto_20200620_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='prior',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='v0.OfferAttr'),
        ),
    ]
