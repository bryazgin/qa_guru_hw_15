from selene import browser, be

def test_about_page_contains_video(open_about_page):
    browser.element('.video').element('[poster="video/duel.jpg"]').should(be.visible)

