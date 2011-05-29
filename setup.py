from setuptools import setup, find_packages

import pkg_resources
from repoze.who.plugins.pam import version

setup(name='repoze.who.plugins.pam',
      namespace_packages=['repoze', 'repoze.who', 'repoze.who.plugins'],
      zip_safe=False,
      include_package_data=True,
      version=".".join(map(str, version)),
      description="""repoze.who.plugins.pam -- PAM Authentication for WSGI Applications

        repoze.who.plugins.pam is a PAM (Pluggable Authentication Module)
        plugin for authenticatining users against the web server's local PAM
        system.""",
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
          'Topic :: System :: Systems Administration :: Authentication/Directory :: PAM',
      ],
      keywords='pam web application server wsgi repoze repoze.who',
      author='Chris AtLee',
      author_email='chris@atlee.ca',
      packages=find_packages(),
      install_requires=[
          'setuptools',
          'repoze.who',
          'pam',
          ],
      )
