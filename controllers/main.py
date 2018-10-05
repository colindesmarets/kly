# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.http import request
from odoo import http

class loginsurvey(http.Controller):
	@http.route(['/'],type='http', auth='user', website=True)
	def default_route(self, **kw):
		values = []
		return request.render("kly.home", values)
