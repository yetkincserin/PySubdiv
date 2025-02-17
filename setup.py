from setuptools import setup, find_packages

setup(
    name="PySubdiv",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "networkx==2.6.3",
        "numpy==1.22.0",
        "pyacvd==0.2.7",
        "pyswarms==1.3.0",
        "pyvista==0.33.0",
        "scipy==1.7.3",
        "pymeshlab==2022.2.post2",
        "pyvistaqt==0.6.0",
        "PyQt5==5.15.6",
        "PyQt5-sip",
        "meshio==5.3.4",
        "QtPy==2.0.0",
        "vtk==9.1.0",
        "setuptools==57.0.0",
        "easygui"
    ],
    url="",
    license="",
    author="Simon Bernard, S. Mohammad Moulaeifard",
    author_email="simon.bernard@rwth-aachen.de, Mohammad.Moulaeifard@cgre.rwth-aachen.de",
    description="An Open-source, Python-based software for fitting subdivision surfaces"
)
