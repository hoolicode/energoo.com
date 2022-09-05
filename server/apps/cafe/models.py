from django.db import models

class Table:
    number = None
    is_busy = None


class Personal:
    full_name = None
    years_experience = None 
    medias = None


class PersonalMedia:
    name = None
    link = None
    class_fa = None
