import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='docker-compose-just-quieter',
    version='0.1',
    author='Linas Valiukas, Media Cloud project',
    author_email='linas@media.mit.edu',
    description='Docker Compose CLI utility wrapper which makes `docker-compose` quieter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/berkmancenter/mediacloud-docker-compose-just-quieter',
    license='Apache License 2.0',
    keywords='docker docker-compose',
    packages=[],
    zip_safe=True,
    install_requires=[
        'docker-compose>=1.25.0,<2.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Software Distribution',
    ],
    python_requires='>=3.5',
    scripts=['docker-compose-just-quieter'],
)
