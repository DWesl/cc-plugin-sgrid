#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from compliance_checker.base import BaseNCCheck, Result, BaseCheck

try:
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'VERSION')) as f:
        __version__ = f.read().strip()
except OSError:
    import glob
    dist_info = glob.glob(os.path.join(os.path.dirname(os.path.dirname(__file__)), "cc_plugin_sgrid*.dist-info"))[0]
    __version__ = os.path.basename(dist_info)[15:-10]
    del glob, dist_info

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class SgridChecker(BaseNCCheck, BaseCheck):
    _cc_spec = 'SGRID'
    _cc_url = 'https://github.com/ioos/cc-plugin-sgrid'
    _cc_author = 'Kyle Wilcox <kyle@axiomdatascience.com>'
    _cc_checker_version = __version__

    @classmethod
    def beliefs(cls): 
        return {}

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        pass
