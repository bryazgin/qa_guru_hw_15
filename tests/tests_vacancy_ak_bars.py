from selene import browser, have


def test_product_owner_vacancy():
    browser.open('/89458847?from=vacancy_search_list&hhtmFrom=vacancy_search_list')

    # WHEN
    browser.element('.vacancy-title').should(have.text('Product Owner'))