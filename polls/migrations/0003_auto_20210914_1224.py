# Generated by Django 2.2.10 on 2021-09-14 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210914_1100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'Пройденный опрос', 'verbose_name_plural': 'Пройденные опросы'},
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='end_data',
            new_name='end_date',
        ),
        migrations.AlterField(
            model_name='answer',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Vote', verbose_name='Опрос пользователя'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='Ответ в свободной форме', max_length=255, verbose_name='Текст ответа'),
        ),
    ]
