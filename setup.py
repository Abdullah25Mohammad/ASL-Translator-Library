from setuptools import find_packages, setup

setup(
    name='ASLTranslator',
    packages=find_packages(include=['ASLTranslator']),
    version='0.1.0',
    description='Using WebCam to translate ASL to English',
    author='Abdullah Mohammad',
    install_requires=['opencv-python', 'numpy', 'mediapipe', 'tf-keras'] 
)