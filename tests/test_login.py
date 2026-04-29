from pages.basic_auth_page import BasicAuthPage

def test_basic_auth(page):
    auth_page = BasicAuthPage(page)

    auth_page.login_and_open("admin", "admin")

    message = auth_page.get_success_message()

    assert "Congratulations! You must have the proper credentials." in message