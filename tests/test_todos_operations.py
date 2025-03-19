from xml.sax.saxutils import escape

from selene import browser, have, be, command

# предимпорт в файле match: have, be
# from selene_in_action.conditions import match
# и вместо have, be всегда использовать match


def test_complete_todo():

    browser.open('/todomvc/dist/')
    browser.element('.new-todo').should(be.blank)

    browser.element('.new-todo').type('a').press_enter()
    '''
    #browser.element('.new-todo').with_(type_by_js=True).type('a').press_enter()
    #browser.element('.new-todo').perform(command.select_all) #в command убраны команды не часто используемые (якобы костыли)
    '''
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()

    browser.all('.todo-list>li').should(have.size(3))
    browser.all('.todo-list>li').first.should(have.exact_text('a'))
    browser.all('.todo-list>li').second.should(have.exact_text('b'))
    browser.all('.todo-list>li')[2].should(have.exact_text('c'))
    browser.all('.todo-list>li')[-1].should(have.exact_text('c'))

    browser.all('.todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    #browser.all('.todo-list>li').second.element('.toggle').click()
    browser.all('.todo-list>li').element_by(have.exact_text('a')).element('.toggle').click()
    browser.all('.todo-list>li').by(have.css_class('completed')).should(have.exact_texts('a'))
    browser.all('.todo-list>li').by(have.no.css_class('completed')).should(have.exact_texts('b','c'))


    '''
    #browser.all('.todo-list>li').with_(timeout=4.0).should(have.size(3)) # установка опции отличной от опции конфига
    #browser.all('.todo-list>li').with_(timeout=browser.config.driver_options*2).should(have.size(3))
    #browser.all('.todo-list>li').wait.for_(have.size(3)) #ждем до тех пор пока не выполнится (have.size(3))
    '''





