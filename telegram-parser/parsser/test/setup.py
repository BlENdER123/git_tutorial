# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('test.py',icon='icon.ico')]

includes = ['time']

zip_include_packages = [ 'time' ]

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
}
}

setup(name='hello_world',
      version='0.0.1',
      description='My Hello World App!',
      executables=executables,
      options=options)