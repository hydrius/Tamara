from setuptools import setup

setup(name='Tamara',
      version='0.0.13',
      packages=['Tamara'],
      #package_dir = {'': 'Tamara'},
      entry_points={
          'console_scripts': [
              'Tamara_py = Tamara.__main__:main'
          ]
      },
      )
