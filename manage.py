#!/usr/bin/env python
import os
import sys
#it will be nice if you could do more
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miniTaobao.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
