# Generated by Django 2.1.3 on 2018-11-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Bad')], default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Read'), (2, 'Unread')]),
        ),
    ]
