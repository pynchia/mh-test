from setuptools import setup, find_packages


# with open('README.rst') as f:
#     LONG_DESC = f.read()

setup(
    name='mh',
    version='1.0.0',
    url='http://example.com',
    description='Test exercise to produce and consume meter and PV readings',
    # long_description=LONG_DESC,
    author='Pynchia', author_email='pyncha@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'],
    keywords=['PV', 'meter', 'broker', 'reading'],
    # packages=find_packages(),
    packages=['mh'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    metercli = mh.meter.cli:cli
    pvcli = mh.pv.cli:cli
    """,
    install_requires=[]
)
