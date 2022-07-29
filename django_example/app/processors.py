import ftd
import ftd_django

from . import views

@ftd_django.processor("todo_title")
def todo_title(doc_id, section, interpreter):
    return ftd.string_to_value("::Simple Todo::")

@ftd_django.processor
def todo_data(doc_id, section, interpreter):
    curr_todo = views.data
    return ftd.object_to_value(curr_todo, section, interpreter)

@ftd_django.processor
def test_data(doc_id, section, interpreter):
    curr_todo = views.test_data
    return ftd.object_to_value(curr_todo, section, interpreter)

@ftd_django.processor
def get_helper_data(doc_id, section, interpreter):
    helper_data = views.helper_data
    return ftd.object_to_value(helper_data, section, interpreter)




