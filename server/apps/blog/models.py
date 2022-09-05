from django.db import models

class Post:
    title = None
    content = None
    thumbnail = None
    is_published = None
    date_publication = None
    date_creation = None


class Comment:
    email = None
    name = None
    content = None
