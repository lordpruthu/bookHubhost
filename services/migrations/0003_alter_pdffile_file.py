# Generated by Django 4.1.7 on 2023-04-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_pdffile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdffile',
            name='file',
            field=models.FileField(upload_to='media/pdfs/'),
        ),
    ]
