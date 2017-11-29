#!/usr/bin/env python

import base64
import os
import json
import sys

domain = sys.argv[1]

data = {
    'FULL_CERT': base64.standard_b64encode(open("certs/config/live/{}/fullchain.pem".format(domain)).read()),
    'PRIVATE_KEY': base64.standard_b64encode(open("certs/config/live/{}/privkey.pem".format(domain)).read()),
}

json_output = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
        "name": "letsencrypt-" + domain.replace('.', '-')
    },
    "type": "Opaque",
    "data": data,
}

print json.dumps(json_output)
