# Generated by Django 5.0.6 on 2024-06-24 23:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('swift_code', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('account_type', models.CharField(choices=[('savings', 'Savings'), ('checking', 'Checking'), ('credit', 'Credit')], max_length=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='api.bank')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, unique=True)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('limit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_cards', to='api.bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_cards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('credit_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.creditcard')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.account')),
            ],
        ),
    ]
