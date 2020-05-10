from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model

from django.contrib.auth.models import User
from rest_framework.test import APIClient

def before_each_feature(feature):
    pass

def step_empty_table(self, model_name):
    pass

def step_create_users(self):
    pass

def step_log_in(self, username, password):
    pass

def step_confirm_log_in(self):
    pass