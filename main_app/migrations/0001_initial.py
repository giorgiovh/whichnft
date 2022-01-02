# Generated by Django 4.0 on 2022-01-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('opensea_url', models.CharField(max_length=10000)),
                ('banner_url', models.CharField(max_length=10000)),
                ('num_editors', models.IntegerField()),
                ('num_traits', models.IntegerField()),
                ('created_date', models.DateField()),
                ('total_sales', models.IntegerField()),
                ('num_nfts', models.IntegerField()),
                ('num_owners', models.IntegerField()),
                ('average_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('seven_day_sales', models.IntegerField()),
                ('has_discord', models.BooleanField()),
                ('has_twitter', models.BooleanField()),
                ('has_instagram', models.BooleanField()),
                ('has_wiki', models.BooleanField()),
                ('description_words', models.IntegerField()),
                ('cluster', models.CharField(max_length=100)),
            ],
        ),
    ]