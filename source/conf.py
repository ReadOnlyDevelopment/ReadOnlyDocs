#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SpongeDocs documentation build configuration file, created by
# sphinx-quickstart on Mon Jan 23 21:01:22 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#
# sponge_docs_theme: Configures Sphinx to use our theme
# jdlinker: To link Javadocs in the documentation
# sphinx.ext.todo: Allows using TODO elements in the documentation
# sphinx.ext.githubpages: Adds .nojekyll to the output directory
extensions = ['readonly_docs_theme',
              'jdlinker', 'sphinx.ext.todo', 'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['.templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ReadOnlyDocs'
copyright = '2020, ReadOnly Mods'
author = 'Org Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- sphinx-intl Configuration --------------------------------------------

# Directories in which to search for additional message catalogs, relative
# to the source directory. The directories on this path are searched by the
# standard gettext module.
locale_dirs = ['../locale/']

# If true, a document’s text domain is its docname if it is a top-level
# project file and its very base directory otherwise.
gettext_compact = False

# -- sphinx-JDLinker Configuration ----------------------------------------

javadoc_links = {
    'https://docs.oracle.com/javase/8/docs/api/': ['java'],
    'https://google.github.io/guava/releases/17.0/api/docs/': ['com.google.common']
}

# Set to true to enable sphinx-JDLinker debug dump.
javadoc_dump = False
