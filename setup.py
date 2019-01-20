from distutils.core import setup

setup(
    name='notpi',
    version='0.1.0',
    author='gentlemans-club',
    author_email='kentsd16@student.uia.no',
    packages=['notpi'],
    python_requires='>=3.5.0',
    install_requires=[
        'pygame',
        'numpy'
    ]
)
