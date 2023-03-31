import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


# Technique Djangoway
class Migration(migrations.Migration):

    initial = True

    dependencies = []
    operations = [
        # pas de création réel car on va renommer l'ancienne table
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Address",
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
                        (
                            "number",
                            models.PositiveIntegerField(
                                validators=[django.core.validators.MaxValueValidator(9999)]
                            ),
                        ),
                        ("street", models.CharField(max_length=64)),
                        ("city", models.CharField(max_length=64)),
                        (
                            "state",
                            models.CharField(
                                max_length=2,
                                validators=[django.core.validators.MinLengthValidator(2)],
                            ),
                        ),
                        (
                            "zip_code",
                            models.PositiveIntegerField(
                                validators=[django.core.validators.MaxValueValidator(99999)]
                            ),
                        ),
                        (
                            "country_iso_code",
                            models.CharField(
                                max_length=3,
                                validators=[django.core.validators.MinLengthValidator(3)],
                            ),
                        ),
                    ],
                    options={
                        "verbose_name_plural": "Adresses",
                    },
                ),
                migrations.CreateModel(
                    name="Letting",
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
                        ("title", models.CharField(max_length=256)),
                        (
                            "address",
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                to="lettings.Address",
                            ),
                        ),
                    ],
                ),
            ],
            # On ne fait rien de concret
            database_operations=[],
        ),
    ]