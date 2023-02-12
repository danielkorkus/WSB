class LoginPage:
    def __init__(self, driver, user, password, login_button):
        self.driver = driver
        self.username_field = user
        self.password_field = password
        self.login_button = login_button

    def enter_username(self, username_user):
        field = self.driver.find_element('id', self.username_field)
        field.clear()
        field.send_keys(username_user)

    def enter_password(self, username_password):
        field = self.driver.find_element('id', self.password_field)
        field.clear()
        field.send_keys(username_password)

    def click_login_button(self):
        field = self.driver.find_element('id', self.login_button)
        field.click()

    def open_page(self):
        self.driver.get('http://www.saucedemo.com/')
