# Generated by Django 4.1.5 on 2023-04-25 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='tourist',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Көрікті жерлер', 'verbose_name_plural': 'Көрікті жерлер'},
        ),
        migrations.AddField(
            model_name='tourist',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourist',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tourist',
            name='cat',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='tourist.category', verbose_name='Категории'),
            preserve_default=False,
        ),
    ]
