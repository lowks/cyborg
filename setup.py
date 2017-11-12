from setuptools import setup

setup(
    name='cyborg',
    version='0.2',
    packages=['cyborg'],
    url='https://github.com/orf/cyborg',
    license='',
    author='Orf',
    author_email='tom@tomforb.es',
    description='Python web scraping framework',
    install_requires=[
        "lxml",
        "aiopipes",
        "aiohttp",
        'cssselect'
    ]
)
