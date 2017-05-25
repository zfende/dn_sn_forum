import datetime

from handlers.base import BaseHandler
from models.comment import Comment



class DeleteCommentsCron(BaseHandler):
    def get(self):
        dc_delete_to = datetime.datetime.now() - datetime.timedelta(days=30)

        deleted_comments = Comment.query(
            Comment.deleted == True, Comment.created <= dc_delete_to
        ).fetch()

        for comment in deleted_comments:
            comment.key.delete()