from pickletools import optimize

from click import option
from selene import browser, have, be

def test_practice_form():
    browser.open("https://demoqa.com/automation-practice-form")
    #executeJavaScript("browser.element('#fixedban').remove()");
    #executeJavaScript("browser.element('footer').remove()");

    browser.element('#firstName').type('Artem')
    browser.element("#lastName").type("Bulaev")
    browser.element("#userEmail").type("Fooolll@test.com")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").type("89649990000")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element([option("4")]).click()
    browser.element(".react-datepicker__year-select").element([option("1990")]).click()
    browser.element(".react-datepicker__day--010").click()
    browser.element("#subjectsInput").type("Maths").press_enter()
    browser.element("#subjectsInput").type("bio").press_enter()
    browser.element("#subjectsInput").type("ch").press_enter()
    browser.element("#hobbiesWrapper").element(have.exact_text("Sports")).click()
    browser.element("#hobbiesWrapper").element(have.exact_text("Music")).click()
    browser.element("#uploadPicture").uploadFromClasspath("img/Test.jpg")
    browser.element("#currentAddress").type("Penza")
    browser.element("#state").click()
    browser.element("#stateCity-wrapper").element(have.exact_text("NCR")).click()
    browser.element("#city").click()
    browser.element("#stateCity-wrapper").element(have.exact_text("Delhi")).click()
    browser.element("#submit").click()

    browser.element(".table-hover").should(have.exact_texts('Artem Bulaev', 'Fooolll@test.com',
                                 'Male', '8964999000'))
    browser.element("#closeLargeModal").click() # прокрутка  для видимости кнопки

    browser.close()