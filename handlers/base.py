import os
import jinja2
import webapp2
import uuid

from google.appengine.api import users
from google.appengine.api import memcache

from models.topic import Topic

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}

        # cookies
        cookie_law = self.request.cookies.get("cookie_law")
        if cookie_law:
            params["cookies"] = True

        # google login
        user = users.get_current_user()
        if user:
            params["user"] = user
            params["logout_url"] = users.create_logout_url('/')
        else:
            params["login_url"] = users.create_login_url('/')

        csrf_token = str(uuid.uuid4())
        memcache.add(key=csrf_token, value=True, time=1200)
        params["csrf_token"] = csrf_token

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        topics = Topic.query(Topic.deleted == False).fetch()
        params = {"topics": topics}
        return self.render_template("main.html", params)

class CookieAlertHandler(BaseHandler):
    def post(self):
        self.response.set_cookie(key="cookie_law", value="accepted")
        return self.redirect("/")