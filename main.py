#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, TopicDetailsHandler, TopicDeleteHandler, SubscribeToTopicHandler
from handlers.comments import CommentAddHandler, CommentsListHandler
from tasks.email_new_comment import EmailNewCommentWorker

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAddHandler, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetailsHandler, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAddHandler, name="comment-add"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDeleteHandler, name="topic-delete"),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="task-email-new-comment"),
    webapp2.Route('/comments/list', CommentsListHandler),
    webapp2.Route('/topic/<topic_id:\d+>/subscribe', SubscribeToTopicHandler),
], debug=True)
