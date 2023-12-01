from selene import browser, be, command


def test_about_page_contains_video(open_about_page):
    browser.element('.video').perform(command.js.scroll_into_view)
    browser.element('.video').element('[poster="video/duel.jpg"]').should(be.visible)

