#!/Users/andy/Desktop/project/Elearning/venv/bin/python
# -*- coding: utf-8 -*-
import re
import sys

from py_translator.urls.py import urls

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(urls.py())
