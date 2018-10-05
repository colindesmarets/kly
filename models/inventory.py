# -*- coding: utf-8 -*-
from odoo import models, fields, api

class resPartner(models.Model):
	_inherit = "res.partner"
	
	session_ids = fields.One2many("story.session", "partner_id", string="Sessions")

class charInventory(models.Model):
	_name = "inventory.inventory"

	item_ids = fields.One2many("inventory.item", "inventory_id", string="Items")
	name = fields.Char(string="Name")

class charItem(models.Model):
	_name = "inventory.item"

	inventory_id = fields.Many2one("inventory.inventory", string="Inventory")
	name = fields.Char(string="Name")
	code = fields.Char(string="Code")

class storyStory(models.Model):
	_name = "story.story"

	name = fields.Char(string="Name")
	session_ids = fields.One2many("story.session", "story_id", string="Sessions")
	chapter_ids = fields.One2many("story.chapter", "story_id", string="Chapters")

class storySession(models.Model):
	_name = "story.session"
	_order = "date, partner_id, story_id"

	inventory_id = fields.Many2one("inventory.inventory", string="Inventory")
	partner_id = fields.Many2one("res.partner", string="Partner")
	story_id = fields.Many2one("story.story", string="Story")
	date = fields.Date(string="Date")

class storyChapter(models.Model):
	_name = "story.chapter"

	name = fields.Char(string="Name")
	event_ids = fields.One2many("story.event", "chapter_id", string="Events")
	story_id = fields.Many2one("story.story", string="Story")

class storyEvent(models.Model):
	_name = "story.event"

	name = fields.Char(string="Name")
	chapter_id = fields.Many2one("story.chapter", string="Chapter")

	text = fields.Text(string="Text")

	has_question = fields.Boolean(string="Has Question")
	question_id = fields.Many2one("story.question", string="Question")

class storyQuestion(models.Model):
	_name = "story.question"

	name = fields.Char(string="Name")
	anwer_ids = fields.One2many("story.answer", "question_id", string="Answer(s)")
	is_open = fields.Boolean(string="Is open")
	open_answer = fields.Char(string="Answer")

class storyAnswer(models.Model):
	_name = "story.answer"

	name = fields.Char(string="Name")
	question_id = fields.Many2one("story.question", string="Question")

