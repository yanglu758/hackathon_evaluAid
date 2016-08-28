#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# foreign imports
import webapp2

# local imports
from controllers.HomeHandler import HomeHandler
from controllers.DashboardHandler import DashboardHandler
from controllers.LoginHandler import LoginHandler
from controllers.ProjectHandler import ProjectHandler
from controllers.DealHandler import DealHandler

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/project', ProjectHandler),
    ('/deal', DealHandler)
], debug=True)