# Generated by Django 3.2.3 on 2021-08-27 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TripModel',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='旅行名')),
                ('tripid', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='管理番号')),
                ('postdate', models.DateField(auto_now_add=True, verbose_name='投稿日')),
                ('category', models.CharField(max_length=50, verbose_name='カテゴリ')),
                ('tripdate', models.DateField(verbose_name='旅行日')),
                ('budget', models.TextField(blank=True, max_length=1000, verbose_name='予算メモ')),
                ('content', models.TextField(blank=True, max_length=2000, verbose_name='旅行メモ')),
                ('images', models.ImageField(blank=True, default='media/noimage.jpg', upload_to='media/', verbose_name='写真(1枚のみ)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='RootModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depspot', models.CharField(max_length=50, verbose_name='出発地点')),
                ('arrspot', models.CharField(max_length=50, verbose_name='到着地点')),
                ('deptime', models.TimeField(verbose_name='出発時間')),
                ('arrtime', models.TimeField(verbose_name='到着時間')),
                ('depdate', models.DateField(null=True, verbose_name='出発日')),
                ('arrdate', models.DateField(null=True, verbose_name='到着日')),
                ('roottitle', models.CharField(blank=True, max_length=50, verbose_name='旅程の概要')),
                ('rootmemo', models.TextField(blank=True, max_length=1000, verbose_name='旅程概要メモ')),
                ('rootcategory', models.CharField(choices=[('train', '列車'), ('shinkansen', '新幹線'), ('bus', 'バス'), ('taxi', 'タクシー'), ('plane', '飛行機'), ('ship', '船'), ('walk', '徒歩'), ('other', 'その他')], max_length=100, verbose_name='旅程カテゴリ')),
                ('rootid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fledit.tripmodel', verbose_name='旅程番号')),
            ],
        ),
    ]
