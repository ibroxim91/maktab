# Generated by Django 3.0.3 on 2020-06-12 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Fan nomi')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Fan nomi')),
                ('query', models.CharField(max_length=950)),
                ('reg_data', models.DateTimeField(auto_now_add=True)),
                ('class_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xtb.Classes')),
                ('predmet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xtb.Predmet')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=550)),
                ('is_answer', models.BooleanField(default=False, verbose_name="To'g'ri javob")),
                ('number', models.PositiveIntegerField(blank=True, default=0)),
                ('reg_data', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xtb.Question')),
            ],
            options={
                'ordering': ['?'],
            },
        ),
    ]
