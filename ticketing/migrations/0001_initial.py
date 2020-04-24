# Generated by Django 3.0.5 on 2020-04-23 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(default='تهران', max_length=50)),
                ('capacity', models.IntegerField()),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('length', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('salable_seats', models.IntegerField()),
                ('free_seats', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'فروش آغاز نشده'), (2, 'در حال فروش بلیت'), (3, 'اتمام بلیت'), (3, 'غیلم پخش شد'), (4, 'سانس لفو شد')])),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.Cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.Movie')),
            ],
        ),
    ]
