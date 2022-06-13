from page_objects.BasePage import BasePage
from helper import write_to_file
import json


def test_get_attrs(browser):
    BasePage(browser).send_text_to_search_field("Red rift")
    BasePage(browser).go_to_site("Red Rift: Home page")
    attributes = BasePage(browser).get_join_our_team_button()
    write_to_file(json.dumps(attributes))
    assert attributes is not None
