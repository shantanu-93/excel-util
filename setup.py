from distutils.core import setup
import py2exe
 
# setup(console=['excelutil.py'])
# setup(windows=[{"script":"excelutil.py"}], options={"py2exe":{"includes":["sip"]}})
setup( windows =[{"script": "excelutil.py"},])


# from distutils.core import setup
# import py2exe, sys, os
# sys.argv.append('py2exe')
# setup(
# options = {'py2exe': {'bundles_files': 1}},
# windows = [{'script': "Driverscript.py"}],
# zipfile = None,)
