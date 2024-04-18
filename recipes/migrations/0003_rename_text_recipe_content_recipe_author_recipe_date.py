# Generated by Django 4.2.11 on 2024-04-17 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.CharField(default='temp', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]