from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

install_requires = [
    'letsencrypt',
    'zope.interface',
    'pymongo',
]

setup(
    name='letsencrypt-pritunl',
    version=version,
    description="Pritunl plugin for Let's Encrypt client",
    url='https://github.com/kharkevich/letsencrypt-pritunl',
    author="Aliaksandr Kharkevich",
    author_email='aliaksandr_kharkevich@outlook.com',
    py_modules = ['pritunl'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license='Apache License 2.0',
    keywords = ['letsencrypt', 'pritunl'],
    entry_points={
        'letsencrypt.plugins': [
            'pritunl = pritunl_pugin.pritunl:PritunlInstaller',
        ],
    },
)
