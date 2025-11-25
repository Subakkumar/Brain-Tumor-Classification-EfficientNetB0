from setuptools import setup, find_packages

setup(
    name="brain-tumor-classification",
    version="1.0.0",
    description="Brain Tumor MRI Classification using EfficientNetB3",
    packages=find_packages(),
    install_requires=[
        'tensorflow-gpu>=2.10.0',
        'opencv-python>=4.7.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.0',
        'pandas>=1.5.0',
        'scikit-learn>=1.2.0',
    ],
    python_requires='>=3.8',
)