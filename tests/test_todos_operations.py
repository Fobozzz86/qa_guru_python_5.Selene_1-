from selene import browser, have, be



def test_complete_todo():


    browser.open('/todomvc/dist/')
    browser.element('.new-todo').should(be.blank)
    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('.toggle').should(have.size(3))