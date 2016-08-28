import jinja2
import os

from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    autoescape=True, extensions=['jinja2.ext.autoescape'],
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname('oneclick0827'), 'templates'))
)


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        # user = users.get_current_user()
        # if user:
        #     nickname = user.nickname()
        #     logout_url = users.create_logout_url('/')
        #     greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
        #         nickname, logout_url)
        # else:
        #     login_url = users.create_login_url('/login')
        #     greeting = '<a href="{}">Sign in</a>'.format(login_url)
        #
        # self.response.write(
        #     '<html><body>{}</body></html>'.format(greeting))
        template = JINJA_ENVIRONMENT.get_template('dashboard.html')
        self.response.out.write(template.render())