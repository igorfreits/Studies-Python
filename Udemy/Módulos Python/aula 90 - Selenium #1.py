"""Selenium - Automatizando tarefas no navegador

Selenium é uma ferramenta para testar sua aplicação web.
Você pode fazer isso de várias maneiras, por exemplo

-Permitir que ele toque nos botões
-Insira o conteúdo nas estruturas
-Dê uma olhada no seu site para verificar se está tudo "OK" e assim por diante.

-https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/
"""
import profile
from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            r'user-data-dir=C:\Users\Igor\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def access(self, site):
        self.chrome.get(site)

    def click_sing_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('error when clicking sign in: ', e)

    def login(self):
        try:
            input_login = self.chrome.find_element_by_id("login_field")
            input_password = self.chrome.find_element_by_id(
                "password")
            btn_login = self.chrome.find_element_by_name("commit")
            input_login.send_keys('Colomk')
            input_password.send_keys('Colomk+4467')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('error when clicking on profile ', e)

    def click_profile(self):
        try:
            profile = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
            profile.click()
        except Exception as e:
            print('error when clicking on profile: ', e)

    def logout(self):
        try:
            profile = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            profile.click()
        except Exception as e:
            print('error when logging out: ', e)

    def check_user(self, user):
        profile_link = self.chrome.find_element_by_class_name(
            'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert user in profile_link_html

    def exit(self):
        self.chrome.quit()


if __name__ == "__main__":
    chrome = ChromeAuto()
    chrome.access('https://github.com/')

    chrome.click_sing_in()
    chrome.login()
    chrome.click_profile()
    sleep(2)
    chrome.check_user('Colomk')
    sleep(10)
    chrome.exit()
