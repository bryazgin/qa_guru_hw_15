from selene import browser, be, have


def test_city_choose_appearance(open_main_page):
    browser.element('[class="modalCity_1hLA5 open_23iHa"]').should(be.visible)


def test_placeholder_in_authorization(open_main_page):
    browser.element('[class="VButton_3W2He _size-xs_rgxyI _blue_2Pdzj button_2jay7"]').click()
    browser.element('[class="signIn_Djdfy"]').should(be.visible).click()
    browser.wait_until(browser.element('[class="r-input login-phone-modal__input"]').should(be.visible))
    browser.element('[class="r-input login-phone-modal__input"]').element('[name="phone"]').should(have.attribute('placeholder','+7 999 999-99-99'))