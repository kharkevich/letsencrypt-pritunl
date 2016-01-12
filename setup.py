import os
from setuptools import setup

version = '0.1.2'

install_requires = [
    'letsencrypt',
    'zope.interface',
    'pymongo',
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='letsencrypt-pritunl',
    version=version,
    author="Aliaksandr Kharkevich",
    author_email='aliaksandr_kharkevich@outlook.com',
    description="Pritunl plugin for Let's Encrypt client",
    license='Apache License 2.0',
    keywords = ['letsencrypt', 'pritunl'],
    url='https://github.com/kharkevich/letsencrypt-pritunl',
    download_url = 'https://github.com/kharkevich/letsencrypt-pritunl/tarball/0.1.2', # I'll explain this in a second
    packages=['pritunl_plugin'],
    long_description=read('README.md'),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    platforms='any',
    entry_points={
        'letsencrypt.plugins': [
            'pritunl = pritunl_plugin.pritunl:PritunlInstaller',
        ],
    },
)
