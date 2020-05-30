from distutils.core import setup

from setuptools import find_packages

setup(
    name='wstomp',
    version='1.0',
    description='STOMP over WebSocket for Python 3',
    author='Hugo Vinícius Sartori',
    author_email='hugo_sart@hotmail.com',
    url='https://github.com/HugoSart/wstomp',
    packages=find_packages(exclude=['wstomp/test']),
    install_requires=['websocket_client', 'rx']
)
