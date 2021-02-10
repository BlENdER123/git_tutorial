# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('parser.py')]

includes = ['requests', 'bs4', 'time', 'telebot']

zip_include_packages = [ 'requests', 'bs4', 'time', 'telebot']

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
}
}

setup(name='parser.py',
version='1',
description='Parser',
executables=executables,
options=options)