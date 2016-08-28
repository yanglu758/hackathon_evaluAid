import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname('oneclick0827'), 'templates')),
)


class DealHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('deal.html')
        self.response.out.write(template.render())
