""" Setup script
"""

from setuptools import setup

setup(
    name='euler',
    version='0.1',
    author='Andrew Berger',
    author_email='andbberger@gmail.com',
    description='System-wide utils',
    url='https://github.com/rueberger/proj_euler',
    packages=['euler'],
    python_requires='>=3.5',
    install_requires=[
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'euler=euler.solver:main'
        ]
    }
)
