from selene import browser, be, command


def test_columbia_image():
    browser.open('https://xn----8sbd2bd3a.xn--p1ai/product.html')
    browser.element('[class="img-block-mobile__page"]').element('[src="/images/columbia.png"]').click()
    browser.element('.btn-block').perform(command.js.scroll_into_view)
    browser.element('[class="img-block-mobile__slider"]').element(
        '[style="display: block;"]').element('[src="/images/site4.png"]').should(be.visible)
