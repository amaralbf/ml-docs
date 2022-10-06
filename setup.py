from setuptools import setup


def README():
    with open('README.md', 'rt', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(
    name='ml-docs',
    version='0.1.0',
    author='Bruno Amaral',
    author_email='amaralbf@gmail.com',
    url='https://github.com/amaralbf/ml-docs',
    project_urls={'Documentation': 'https://amaralbf.github.io/ml-docs/'},
    description=('A library for documentation of data science projects.'),
    long_description=README(),
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=['ml_docs'],
    python_requires='>=3.7,<4.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
