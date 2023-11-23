from selene import browser, be


def test_city_choose_appearance(close_browser,setup_browser):
    browser.open('')
    browser.element('[class="modalCity_1hLA5 open_23iHa"]').should(be.visible)


