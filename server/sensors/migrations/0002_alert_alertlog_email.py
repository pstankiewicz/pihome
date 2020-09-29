# Generated by Django 3.1.1 on 2020-09-28 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('P', 'periodic'), ('O', 'onetime')], max_length=1)),
                ('name', models.CharField(max_length=64)),
                ('active', models.BooleanField()),
                ('period_minutes', models.IntegerField(blank=True, null=True)),
                ('trigger_type', models.CharField(choices=[('eq', 'equals'), ('ne', 'not equals'), ('gt', 'greater than'), ('gte', 'greater than or equals'), ('lt', 'less than'), ('lte', 'less than or equals')], max_length=3)),
                ('trigger_count_for_email', models.IntegerField(default=1)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.alert')),
            ],
        ),
        migrations.CreateModel(
            name='AlertLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('trigger_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('trigger_type', models.CharField(max_length=64)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.alert')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor')),
            ],
        ),
    ]