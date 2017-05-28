import os
import unittest
import webapp2
import webtest
from handlers.topics import TopicAddHandler

from google.appengine.ext import testbed
from google.appengine.api import memcache

from models.topic import Topic



class TopicAddTests(unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication(
            [
                webapp2.Route('/topic/add', TopicAddHandler),
            ])

        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        """ Uncomment the stubs that you need to run tests. """
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # self.testbed.init_mail_stub()
        # self.testbed.init_taskqueue_stub()
        self.testbed.init_user_stub()
        # ...

        """ Uncomment if you need user (Google Login) and if this user needs to be admin. """
        os.environ['USER_EMAIL'] = 'some.user@example.com'
        # os.environ['USER_IS_ADMIN'] = '1'

    def tearDown(self):
        self.testbed.deactivate()

    def test_topic_add_handler(self):
        # Testing GET response
        get_response = self.testapp.get('/topic/add')  # get main handler
        self.assertEqual(get_response.status_int, 200)  # if GET request was ok, it should return 200 status code


        # Testing POST response
        csrf_token ="abc123"
        memcache.add(key=csrf_token, value=True)
        params = {
            "title": "To je testna tema",
            "text": "To je vsebina testne teme.",
            "csrf_token": csrf_token,
        }
        post_response = self.testapp.post('/topic/add', params)
        self.assertEqual(post_response.status_int, 200)

        topics = Topic.query().fetch()
        self.assertEqual(len(topics), 1)
        topic = topics[0]
        self.assertEqual(topic.title, "To je testna tema")