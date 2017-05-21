import cgi

from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment
from utils.decorators import validate_csrf


class CommentAddHandler(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        user = users.get_current_user()
        if not user:
            return self.write("Please login.")

        text = cgi.escape(self.request.get("comment-text"))

        topic = Topic.get_by_id(int(topic_id))
        new_comment = Comment.create(text, user, topic)

        return self.write("Comment created successfully.")
