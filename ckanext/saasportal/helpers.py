"""
Copyright (c) 2016 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging

import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)


def is_admin():
    permissions = toolkit.get_action('organization_list_for_user')(data_dict={'permission': 'admin'})
    if len(permissions) != 0:
        return True
    return False
