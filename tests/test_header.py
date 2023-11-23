from selene import browser, have

def test_contacts_correct_url(open_main_page):
    browser.element('[class ="container navigation_down_1ky4R"]').element('[href="/contacts/"]').click()
    browser.should(have.url('https://samolet.ru/contacts/'))

