from setuptools import setup

setup(
    name="django-redis-cache",
    url="http://github.com/sebleier/django-redis-cache/",
    author="Sean Bleier",
    author_email="sebleier@gmail.com",
    version="2.1.3",
    license="BSD",
    packages=["redis_cache", "redis_cache.backends"],
    description="Redis Cache Backend for Django",
    install_requires=['redis<4.0'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
    ],
)
