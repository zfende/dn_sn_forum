from handlers.base import BaseHandler
from google.appengine.api import mail


class EmailNewCommentWorker(BaseHandler):
    def post(self):
        topic_author_email = self.request.get("topic.author_email")
        topic_title = self.request.get("topic_title")
        topic_id = self.request.get("topic_id")

        mail.send_mail(
            sender="zfende@gmail.com",
            to=topic_author_email,
            subject="Your topic received a new comment",
            body="""Your topic with title %s has a new comment."

<a href='/topic/%s'>Link to the topic</a>""" % (topic_title, topic_id)
        )