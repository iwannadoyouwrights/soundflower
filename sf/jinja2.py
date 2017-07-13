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


# class SfJinjaLoader(BaseLoader):
#     is_usable = True
#
#     env = Environment(loader=FileSystemLoader(get_app_template_dirs))
#     env.template_class = Template
#
#     env.globals['url'] = reverse
#     env.globals['STATIC_URL'] = settings.STATIC_URL
#     env.globals['MEDIA_URL'] = settings.MEDIA_URL
#
#     def load_template(self, template_name, template_dirs=None):
#         try:
#             template = self.env.get_template(template_name)
#         except TemplateNotFound:
#             raise TemplateDoesNotExist(template_name)
#         return template, template.filename