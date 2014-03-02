from setuptools import setup

setup(
    name='microq',
    version='0.1',
    description='A simple multi-producer, -consumer, -threaded queue leveraging microrpc.',
    author='Jason Johnson',
    author_email='spligak@gmail.com',
    packages=['microq'],
    install_requires=['microrpc'],
    license='MIT',
    zip_safe=False,
    url='http://github.com/jasonjohnson/microq'
)

