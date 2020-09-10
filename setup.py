from setuptools import (
    setup, find_packages)

from kaalia import (
    __version__ as VERSION,
    __title__ as TITLE)

with open('README.md') as f:
    README = f.read()

OPTS = dict(
    name='kaalia',
    version=VERSION,
    description=TITLE,
    author='Rachel Snyder',
    author_email='rachelmassey29@gmail.com',
    packages=find_packages(),
    package_dir={'kaalia': 'kaalia'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pysdl2',
        'pyopengl'
    ]
)

if __name__ == '__main__':
    setup(**OPTS)
