from setuptools import setup

setup(name='darkskypy',
      version='0.1d',
      description='Python wrapper for darksky.net weather service',
      url='https://github.com/PvtHaggard/darkskypy',
      author='PvtHaggard',
      author_email='pvthaggard@gmail.com',
      license='GPLv3',
      packages=['darkskypy'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
