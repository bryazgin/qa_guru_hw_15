from selene import browser, command, by, be, have


def test_can_go_from_mission_to_timeback(open_company_page):
    browser.element('[class="r-about-mission__header"]').element(by.text('О компании')).perform(command.js.scroll_into_view)
    browser.element('[href="/timeback/"]').click()
    browser.should(have.url('https://samolet.ru/timeback/'))
    browser.element('[class="timeback-intro__col _text"]').should(be.visible)