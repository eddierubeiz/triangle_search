# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0002_auto_20160301_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='triangleissue',
            old_name='notes_1',
            new_name='ocr_text',
        ),
    ]
