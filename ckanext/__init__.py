#!/usr/bin/env python3
# encoding: utf-8
#
# This file is part of ckanext-contact
# Created by the Natural History Museum in London, UK

try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)
