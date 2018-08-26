from selenium import webdriver


class Browser(object):

    #Path to your chromedriver
    driver = webdriver.Chrome(executable_path="D:/nauka/chromedriver")
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()