import setuptools

setuptools.setup(
    name='qarray',
    version='0.0.0',
    license='Apache 2.0',
    install_requires=['xarray', 'sqlglot'],
    extras_require={
        'dev': ['pyink'],
    },
    python_requires='>=3.9',
)