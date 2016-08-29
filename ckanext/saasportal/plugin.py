import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from helpers import is_admin

log = logging.getLogger(__name__)


class SaasportalPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'saasportal')

    def get_helpers(self):
        return {'saasportal_is_admin': is_admin}
