from time import sleep
from .pages.sbis_contacts_page import SbisContactsPage


def test_can_change_region(browser):
    link = "https://sbis.ru/contacts/"
    page = SbisContactsPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    region_text = page.home_region_text()
    assert 'Нижегородская' in region_text, "Home region does not match"
    partners_text = page.partners_header()
    page.open_popup_regions()
    browser.implicitly_wait(5)
    page.select_region('Камчатский край')
    sleep(1)
    assert 'kamchatskij' in browser.current_url and 'Камчатский' in browser.title, "url and title have not changed according to new region"
    new_partners_text = page.partners_header()
    assert partners_text != new_partners_text, "Partners list has not changed according to new region"
