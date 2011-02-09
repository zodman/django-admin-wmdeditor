from setuptools import setup, find_packages
 
version = '0.0.1'
  
LONG_DESCRIPTION = """
  =====================================
  django-admin-wmdeditor
  =====================================
  Adds markdown wysiwym widget for textareas in djangos admin interface.
"""
   
setup(
           name='django-admin-wmdeditor',
           version=version,
           description="django-admin-wmdeditor",
           long_description=LONG_DESCRIPTION,
           classifiers=[
                       "Programming Language :: Python",
                       "Topic :: Software Development :: Libraries :: Python Modules",
                       "Framework :: Django",
                       "Environment :: Web Environment",
                   ],
           keywords='forms,django,admin,editor',
           author='Steph',
           author_email='mail+web@sjaekel.com',
           url='http://github.com/zodman/django-admin-wmdeditor',
           license='MIT',
           packages = ["admin_wmdeditor"],
           package_dir = {"admin_wmdeditor": 'admin_wmdeditor'},
           include_package_data=True,
           zip_safe=False,
)

