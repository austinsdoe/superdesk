# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

"""
A module containing configuration of the Superdesk's public API.

The meaning of configuration options is described in the Eve framework
`documentation <http://python-eve.org/config.html#global-configuration>`_.
"""


MONGO_DBNAME = 'superdesk'  # XXX: read from superdesk settings?

DOMAIN = {

    # TODO: add endpoint for packages (type: composite)

    'items': {
        'datasource': {
            'source': 'archive'
        }
    },

    # we need this so that the archive collection is accessible from
    # other (public) API endpoints
    # XXX: is it possible to somehow get rid of this?
    'archive': {
        'internal_resource': True
    }
}

# Example of an ID of an object in database (whitout quotes):
#
#     "tag:localhost:2015:f4b35e12-559b-4a2b-b1f2-d5e64048bde8"
#
ITEM_URL = 'regex("(\w|[:-])+")'
