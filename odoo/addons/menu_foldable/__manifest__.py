# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Foldable Menu',
    'category': 'Extra Tools', 
    'version': '10.0.1.1.0',
    'summary': "To Fold and Collapse the Left side Menus in Odoo",
    'description': 'no_warning',
    'author': 'Murali Krishna Reddy',
    'contributors': [
        'Murali Krishna Reddy',
        'Alix Casari',
    ],
    'website': 'http://www.credativ.in',
    'sequence': 0,
    'depends': ['base', 'web'],
    'data': [
        'templates/foldable.xml',
    ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
