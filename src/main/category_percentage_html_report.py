__author__ = 'ferzerkerx'

import os

from jinja2 import Template


def render_contribution_percentage_by_committer_using_categories(stats_by_category):
    layout_template = get_template('layout.html')
    category_percentage_template = get_template('category_percentage.html')
    directory_percentages_template = get_template('directory_percentages.html')

    category_html = ''
    for category_stats in stats_by_category:
        context_data = {'category_stats': category_stats,
                        'directory_percentages_template': directory_percentages_template}
        category_html += category_percentage_template.render(context_data)
    return layout_template.render({'content': category_html})


def get_template(template_name=None):
    template_path = get_templates_path()
    f = open(template_path + '/' + template_name, 'r')
    return Template(f.read())


def get_templates_path():
    path_project = os.path.realpath(os.path.dirname(__file__))
    template_path = os.path.join(path_project, '..', 'templates')
    return template_path
