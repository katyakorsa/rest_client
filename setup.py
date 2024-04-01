from distutils.core import setup

REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest',
]

setup(
    name='rest_client',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/katyakorsa/rest_client.git',
    license='MIT',
    author='Ekaterina Korsakova',
    author_email='-',
    install_requires=REQUIRES,
    description='rest client with allure and logger'
)
