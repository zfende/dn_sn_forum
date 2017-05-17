#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, TopicDetailsHandler
from handlers.comments import CommentAddHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAddHandler, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetailsHandler, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAddHandler, name="comment-add"),
], debug=True)
