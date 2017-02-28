from setuptools import setup

setup(name='Tamara',
      version='0.0.1',
      packages=['Tamara'],
      entry_points={
          'console_scripts': [
              'Tamara_py = Tamara.Tamara:main'
          ]
      },
      )
