# Generated by Django 4.1.7 on 2023-04-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_pdffile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='title',
            field=models.CharField(default=str, max_length=255),
            preserve_default=False,
        ),
    ]
