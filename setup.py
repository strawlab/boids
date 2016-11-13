from setuptools import setup

setup(
    name='inconvergentboids',
    license='MIT',
    description='More or less an implementation of Boids flocking algorithm.',
    version='0.0.1',
    package_dir={'inconvergentboids': 'modules'},
    py_modules=['inconvergentboids.boids'],
)
