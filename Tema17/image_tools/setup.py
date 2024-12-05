from setuptools import setup, find_packages

setup(
    name="image_tools",
    version="0.1.0",
    author="Tu Nombre",
    author_email="tuemail@example.com",
    description="Paquete para procesamiento básico de imágenes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/image_tools",
    packages=find_packages(),
    install_requires=[
        "Pillow==10.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
