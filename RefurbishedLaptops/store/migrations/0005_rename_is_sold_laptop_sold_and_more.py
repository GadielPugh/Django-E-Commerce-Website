# Generated by Django 5.1.3 on 2024-11-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_transaction_bank_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='is_sold',
            new_name='sold',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_type',
            field=models.CharField(default='debit card', max_length=50),
        ),
        migrations.AddField(
            model_name='transaction',
            name='pickup_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='laptops/'),
        ),
    ]