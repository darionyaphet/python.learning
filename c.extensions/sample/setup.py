from distutils.core import setup, Extension

setup(name='sample',
      ext_modules=[
        Extension('sample',
                  ['sample.c'],
                  include_dirs = ["/Users/darion.yaphet/repo/python.learning/c.extensions/sample"],
                  define_macros = [('FOO','1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['lib'],
                  libraries = ['sample']
                  )
        ]
)
