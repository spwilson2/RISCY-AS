from setuptools import setup, find_packages

setup(
        name='riscyas',
        version='0.6.0',

        author = 'Sean Wilson',
        author_email = 'spwilson27@gmail.com',
        description = 'An elementary assembler for the RISC-V ISA.',
        license = 'MIT',
        url = 'https://github.com/spwilson2/RISCY-AS',

        packages = find_packages(),
        install_requires=['Click', 'bitstruct'],
        include_package_data = True,

        entry_points= '''
        [console_scripts]
        riscyas=riscyas.assemble:cli
        ''',

        test_suite='nose.collector',
        tests_require=['nose'],

        )
