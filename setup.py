from setuptools import setup

setup(name='MiAgDa',
      version='0.0.1',
      description='Minimalistic Agile Dashboard',
      url='https://github.com/HaBaLeS/MiAgDa',
      author='falko lehmann',
      author_email='falko@lehmann-carpzov.de',
      license='beer',
      packages=['miagda'],
      install_requires=['pygame'],
      scripts=['bin/miagda-run'],
      zip_safe=False)