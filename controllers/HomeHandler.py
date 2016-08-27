import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    autoescape=True, extensions=['jinja2.ext.autoescape'],
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname('oneclick0827'), 'templates'))
)


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'test_value': ""
        }

        if 'APPROVED' == 'APPROVED':
            template_values['test_value'] = "Payment approved"
        else:
            template_values['test_value'] = "Payment denied"

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
