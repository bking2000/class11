#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

setup(
    name = "air_sea",
    version = "0.0.1",
    author = "Brendan King",
    packages=['sat_vp'],
    install_requires=['numpy','scipy.io'],
)

