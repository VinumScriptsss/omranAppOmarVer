# Generated by Django 4.1.7 on 2023-03-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='isActive',
            field=models.BooleanField(default=True, help_text='activer ou desactiver ce produit', verbose_name='status de produit'),
        ),
    ]