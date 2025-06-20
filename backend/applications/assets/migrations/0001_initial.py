# Generated by Django 5.2 on 2025-06-01 21:27

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_data', '0002_metaltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('estimated_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('estimated_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('weight_in_grams', models.FloatField()),
                ('weight_unit', models.CharField(choices=[('gram', 'Gramo'), ('kilogram', 'Kilogramo'), ('onza', 'onza'), ('ton', 'Tonelada')], default='gram', max_length=20)),
                ('purity', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('certification', models.CharField(blank=True, max_length=100, null=True)),
                ('metal_form', models.CharField(choices=[('bar', 'Bar'), ('ingot', 'Lingote'), ('grain', 'grain'), ('wire', 'Cable'), ('wasted', 'Desperdicio')], default='wasted', max_length=30)),
                ('metal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_data.metaltype')),
            ],
            options={
                'verbose_name': 'Metal',
                'verbose_name_plural': 'Metals',
                'db_table': 'metals',
            },
        ),
    ]
