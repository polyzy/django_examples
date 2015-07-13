import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('Python', 1280, 640)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://doc.python.org/2/tutorial/")

    add_page(cat=python_cat,
             title="Baidu",
             url="http://www.baidu.com")

    add_page(cat=python_cat,
             title="Weibo",
             url="http://www.weibo.com")

    django_cat = add_cat("Django", 666, 320)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="docs.djangoproject.com/en/1.7")

    add_page(cat=django_cat,
             title="tango with Django",
             url="http://www.tangowithdjango.com")

    frame_cat = add_cat("Other Frameworks", 320, 169)

    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org")

    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org")


    crawl_cat = add_cat("Crawl",1000,500)

    add_page(cat=crawl_cat,
             title="requests",
             url="http://requests.org")

    add_page(cat=crawl_cat,
             title="urllib",
             url="http://url.com")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c

if __name__ == "__main__":
    print "Start Rango population script..."
    populate()
