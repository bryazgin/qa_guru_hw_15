from selene import browser, have, be


def test_open_main_page(open_main_page):
    browser.should(have.url('https://smlab.digital/'))
    browser.element('.slider_new').should(be.visible)

def test_slider_have_needed_image(open_main_page):
    browser.element('[class=slider_new]').element('[src="/images/name.png"]').should(be.visible)


def test_right_number_of_accreditation(open_main_page):
    browser.element('.info-block').element('.col').element('[href="/accreditation.html"]').should(have.text(
        "АО-20220516-4545119877-3"))