from django.db import migrations, models
import django.db.models.deletion


def separate_collections(apps, schema_editor):
    Bin = apps.get_model('bins', 'Bin')
    BinOperation = apps.get_model('bins', 'BinOperation')
    Operation = apps.get_model('bins', 'Operation')
    db_alias = schema_editor.connection.alias

    collection_operation = Operation(name="collection")
    collection_operation.save()
    BinOperation.objects.using(db_alias).bulk_create(
        [BinOperation(operation=collection_operation, bin=_bin,
                      operation_frequency=_bin.collection_frequency,
                      last_operation=_bin.last_collection)
         for _bin in Bin.objects.all()])


def merge_collections(apps, schema_editor):
    BinOperation = apps.get_model('bins', 'BinOperation')
    Operation = apps.get_model('bins', 'Operation')
    db_alias = schema_editor.connection.alias

    collection_operation = Operation.objects.using(db_alias).filter(name="collection")[0]
    bin_collections = BinOperation.filter(operation=collection_operation)

    for collection in bin_collections:
        collection.bin.update(last_collection=collection.last_operation,
                              collection_frequency=collection.operation_frequency)


class Migration(migrations.Migration):

    dependencies = [
        ('bins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BinOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_frequency', models.IntegerField()),
                ('last_operation', models.DateTimeField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bins.bin')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bins.operation')),
            ],
        ),
        migrations.RunPython(separate_collections, merge_collections),
        migrations.RemoveField(
            model_name='bin',
            name='collection_frequency',
        ),
        migrations.RemoveField(
            model_name='bin',
            name='last_collection',
        ),

    ]
