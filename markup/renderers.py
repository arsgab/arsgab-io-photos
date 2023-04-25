from random import randint

from jinja2 import Environment
from pelican import ArticlesGenerator, signals

from markup import renderer_ref
from markup.processors.picture import render_picture_tag
from utils.staticfiles import get_static_url
from utils.templating import render_page_metadata

GLOBALS = {
    'random': randint,
    'static': get_static_url,
    'picture': render_picture_tag,
    'pagemeta': render_page_metadata,
}


def setup_jinja_env(generator: ArticlesGenerator) -> Environment:
    generator.env.globals.update(GLOBALS)
    renderer_ref.set(generator.env)
    return generator.env


def register() -> None:
    signals.article_generator_preread.connect(setup_jinja_env)
    signals.page_generator_preread.connect(setup_jinja_env)
