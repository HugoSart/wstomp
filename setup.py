from distutils.core import setup

from setuptools import find_packages

setup(
    name='wstomp',
    version='1.0',
    description='STOMP over WebSocket for Python 3',
    author='Hugo Vinícius Sartori',
    author_email='hugo_sart@hotmail.com',
    url='https://bitbucket.org/seebotteam/seebot-unify-python',
    packages=find_packages(exclude=['wstomp/test']),
    install_requires=['websocket_client', 'rx']
)
