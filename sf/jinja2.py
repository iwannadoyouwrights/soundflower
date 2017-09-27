from django.template.backends.jinja2 import Jinja2
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from main import views as main_views


class SfJinja2(Jinja2):
    app_dirname = 'jinja2'


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            'static': staticfiles_storage.url,
            'url': reverse,
            'views': main_views,
        }
    )
    return env
