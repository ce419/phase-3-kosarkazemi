from __future__ import absolute_import, unicode_literals

# from celery import Celery

from .celery import app as celery_app

__all__ = ['celery_app']

default_app_config = 'P3.app.P3Config'

# app = Celery('testcele', backend='amqp', broker='redis',include=['author.tasks'])