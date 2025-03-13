from selene import browser, have, be

# предимпорт в файле match: have, be
# from selene_in_action.conditions import match
# и вместо have, be всегда использовать match


def test_complete_todo():

    browser.open('/todomvc/dist/')
    browser.element('.new-todo').should(be.blank)

    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('.todo-list>li').with_(timeout=4.0).should(have.size(3)) # установка опции отличной от опции конфига
    #browser.all('.todo-list>li').with_(timeout=browser.config.driver_options*2).should(have.size(3))

