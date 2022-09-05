from django.db import models


class Product:
    title = None
    content = None
    price = None
    images = None
    weight = None
    dimension_x = None
    dimension_y = None
    dimension_z = None
    sizes = None
    warranty = None


class Size:
    name = None


class ProductPhoto:
    photo = None


class Settings:
    support_phone = None
    support_email = None
    allow_reservation = None


class Order:
    products = None
    price = None