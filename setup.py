from setuptools import setup, find_packages

setup(name='Tamara',
      version='0.2.1',
      #packages=['Tamara'],
      #package_dir = {'': 'sensors'},
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'Tamara_py = Tamara.__main__:main'
          ]
      },
      )
