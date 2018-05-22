from setuptools import setup, find_packages

setup(name='MiAgDa',
      version='0.0.3',
      description='Minimalistic Agile Dashboard',
      url='https://github.com/HaBaLeS/MiAgDa',
      author='falko lehmann',
      author_email='falko@lehmann-carpzov.de',
      license='beer',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['pygame','toml'],
      scripts=['bin/miagda-run'],
      zip_safe=True)