from setuptools import setup


setup(
    name='todoit',
    version='1.0',
    description='CLI todo list',
    author='Enkot',
    install_requires=['click', 'peewee'],
    entry_points={
        'console_scripts': [
            'todoit=todoit:cli',
        ]
    },
)
