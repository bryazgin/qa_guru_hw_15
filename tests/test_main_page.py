from selene import browser, have, be


def test_open_main_page(open_main_page):
    browser.should(have.url('https://xn----8sbd2bd3a.xn--p1ai/'))
    browser.element('.slider_new').should(be.visible)

def test_slider_have_needed_image(open_main_page):
    browser.element('[class=slider_new]').element('[src="/images/name.png"]').should(be.visible)


def test_right_accreditation(open_main_page):
    browser.element('.info-block').element('.col').element('[href="/accreditation.html"]').should(have.text(
        "от 16.05.2022 № \"АО-20220516-4545119877-3"))