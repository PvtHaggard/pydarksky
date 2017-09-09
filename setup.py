from setuptools import setup

setup(name='pydarksky',
      version='1.0',
      description='Python wrapper for darksky.net weather service',
      url='https://github.com/PvtHaggard/pydarksky',
      author='PvtHaggard',
      author_email='pvthaggard@gmail.com',
      license='GPLv3',
      packages=['pydarksky'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
