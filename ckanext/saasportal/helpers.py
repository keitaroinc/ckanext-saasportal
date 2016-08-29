import logging

import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)


def is_admin():
    permissions = toolkit.get_action('organization_list_for_user')(data_dict={'permission': 'admin'})
    if len(permissions) != 0:
        return True
    return False
