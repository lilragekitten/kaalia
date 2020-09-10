from setuptools import (
    setup, find_packages
)

from kaalia_etc import config

with open('README.md') as f:
    README = f.read()

OPTS = dict(
    name='kaalia',
    version=config.ENGINE_CONFIG['version'],
    description=config.ENGINE_CONFIG['title'],
    author='Rachel Snyder',
    author_email='rachelmassey29@gmail.com',
    packages=find_packages(),
    package_dir={
        'kaalia': 'kaalia',
        'kaalia_etc': 'kaalia_etc'
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pysdl2',
        'pyopengl'
    ]
)

if __name__ == '__main__':
    setup(**OPTS)
