from django.db import migrations


def swap_description_comment(apps, schema_editor):
    Product = apps.get_model("browse", "Product")

    for product in Product.objects.all():
        temp = product.description
        product.description = product.comment
        product.comment = temp
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ("browse", "0003_alter_product_comment_alter_product_description"),
    ]

    operations = [
        migrations.RunPython(swap_description_comment),
    ]
