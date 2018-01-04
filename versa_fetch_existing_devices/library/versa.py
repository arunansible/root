#!/usr/bin/python
# -*- coding: utf-8 -*-
''' versa ansible module '''

import base64
import yaml

try:
    import ruamel.yaml as yaml
except ImportError:
    import yaml

from ansible.module_utils.basic import AnsibleModule

class VersaException(Exception):  # pragma: no cover
    ''' Exception class for Yedit '''
    pass
