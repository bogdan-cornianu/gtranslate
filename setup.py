from setuptools import setup

setup(name='gtranslate',
      version='0.1',
      description='CLI for Google Translate',
      url='https://github.com/bogdan-cornianu/gtranslate',
      author='Bogdan Cornianu',
      author_email='bogdan@bogdancornianu.com',
      license='GPLv3',
      packages=['gtranslate'],
      install_requires=[
          'python-daemon==2.2.3',
      ],
      zip_safe=False,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
        'console_scripts': ['gtranslate=gtranslate.gtranslate:main'],
      })
