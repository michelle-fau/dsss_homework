from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="1.0.0",
    description="A simple math quiz game with unit tests",
    author="Michelle",
    author_email="chelle.michelle@fau.de",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

