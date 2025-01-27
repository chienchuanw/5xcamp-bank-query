# Generated by Django 5.0.6 on 2024-06-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0004_rename_bank_name_branch_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='website',
        ),
        migrations.AddField(
            model_name='bank',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='announcement_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='update_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
