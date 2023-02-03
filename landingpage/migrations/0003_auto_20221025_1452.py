# Generated by Django 2.2.12 on 2022-10-25 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_barang_waktu_posting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailtrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('kodebrg', models.CharField(max_length=8)),
                ('qty', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('tgltrans', models.DateTimeField(auto_now_add=True)),
                ('total', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='barang',
            name='waktu_posting',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
