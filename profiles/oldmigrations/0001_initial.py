from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# Djangoway
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # pas de création réel car on va renommer l'ancienne table
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Profile",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("favorite_city", models.CharField(blank=True, max_length=64)),
                        (
                            "user",
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                    ],
                ),
            ],
            # On ne fait rien de concret
            database_operations=[],
        ),
    ]
