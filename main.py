#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, TopicDetailsHandler, TopicDeleteHandler, SubscribeToTopicHandler
from handlers.comments import CommentAddHandler, CommentsListHandler, CommentDeleteHandler
from tasks.email_new_comment import EmailNewCommentWorker
from crons.delete_topics import DeleteTopicsCron
from crons.delete_comments import DeleteCommentsCron


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
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron),
    webapp2.Route('/comment/<comment_id:\d+>/delete', CommentDeleteHandler, name="comment-delete"),
    webapp2.Route("/cron/delete-comments", DeleteCommentsCron, name="cron-delete-comments"),
], debug=True)
