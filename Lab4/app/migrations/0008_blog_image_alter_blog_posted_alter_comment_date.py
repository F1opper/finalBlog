# Generated by Django 4.2.7 on 2023-12-16 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_blog_posted_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 16, 15, 7, 27, 268357), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(db_index=True, default=datetime.datetime(2023, 12, 16, 15, 7, 27, 268357), verbose_name='Дата комментария'),
        ),
    ]
