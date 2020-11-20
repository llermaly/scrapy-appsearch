import ast
import re
from distutils.core import setup
from setuptools import find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('scrapyappsearch/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(name='ScrapyAppSearch',
      version=version,
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allow you to store multiple scrapy items in AppSearch.',
      long_description=open('README.md').read(),
      author='Gustavo Llermaly, Jay Zeng, Michael Malocha, Julien Duponchelle',
      author_email='gllermaly@gmail.com, jayzeng@jay-zeng.com, michael@knockrentals.com, julien@duponchelle.info',
      url='https://github.com/llermaly/scrapy-appsearch.git',
      download_url='https://github.com/llermaly/scrapy-appsearch/archive/0.1.0.tar.gz',
      keywords='scrapy appsearch',
      packages=find_packages(),
      platforms=['Any'],
      install_requires=['scrapy', 'elastic_enterprise_search'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: No Input/Output (Daemon)',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python']
      )