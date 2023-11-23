from selene import browser, be, have

def test_clickable_button(open_company_page):
    browser.element('[class="navigation_down_left_name_31iwB"]').should(be.clickable)
    browser.element('[class="navigation_down_left_name_31iwB"]').click()
    browser.should(have.url('https://samolet.ru/'))
