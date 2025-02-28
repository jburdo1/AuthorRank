from setuptools import setup

setup(
    name='author_rank',
    packages=['author_rank'],
    version='joe1',
    description='',
    author='Valentino Constantinou, Annie Didier',
    author_email='sdwingnut@gmail.com',
    url='https://github.com/jburdo1/AuthorRank',
    download_url='https://github.com/jburdo1/AuthorRank/dist/author_rank-0.1.2.tar.gz',
    keywords=['author_rank', 'PageRank', 'network', 'graph', 'edges', 'nodes', 'authorship', 'AuthorRank'],
    classifiers=[],
    license='MIT',
    install_requires=['networkx', 'python-utils', 'scipy']
)
