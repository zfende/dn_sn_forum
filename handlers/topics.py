import cgi

from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment
from utils.decorators import validate_csrf


class TopicAddHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("Please login.")

        title = cgi.escape(self.request.get("title"))
        text = cgi.escape(self.request.get("text"))

        new_topic = Topic(title=title, content=text, author_email=user.email())
        new_topic.put()

        return self.write("Topic created successfully.")


class TopicDetailsHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == topic.key.id(),
                   Comment.deleted == False).order(Comment.created).fetch()

        params = {"topic": topic, "comments": comments}

        return self.render_template("topic_details.html", params=params)


class TopicDeleteHandler(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        topic_del = Topic.get_by_id(int(topic_id))

        user = users.get_current_user()

        if topic_del.author_email == user.email() or users.is_current_user_admin():
            Topic.delete(topic=topic_del)

        return self.write("Topic deleted successfully.")