from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
