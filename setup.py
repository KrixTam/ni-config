from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ni-config',
    version='0.0.12',
    packages=['ni', 'ni.config'],
    url='https://github.com/KrixTam/ni-config',
    license='MIT',
    author='Krix Tam',
    author_email='krix.tam@qq.com',
    description='把json文件当作配置文件使用时，为了方便对配置文件进行操作而创建的配置文件类库',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/KrixTam/ni-config/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["config"],
    python_requires=">=3.6",
    install_requires=[
        'jsonschema>=3.2.0',
        'pyyaml>=5.4.1',
        'cryptography>=3.4.7'
    ]
)
