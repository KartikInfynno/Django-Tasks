# Generated by Django 4.0.6 on 2022-07-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0003_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('shoes', 'shoes'), ('jacket', 'jacket'), ('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('bag', 'bag'), ('glasses', 'glasses'), ('others', 'others')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
