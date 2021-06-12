from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from helpers import By, Keys


def example_special_function(driver: WebDriver):
    print(f"CURRENT URL: {driver.current_url}")
    """ You can even send keystrokes using element.send_keys"""
    return 0


class WebContent:
    """ A object that returns a key and value pair for the content defined 
    Content is defined as :
    by.attr, attr_value, dict_key, special_function
    special function is optional, runs before the data is extracted
    """

    def __init__(self, url, by_attr, attr_value, dict_key, special_function=example_special_function) -> None:
        
        self.url: str = url
        self.by_attr: str = by_attr
        self.attr_value: str = attr_value
        self.dict_key: str = dict_key
        self.special_function: function = special_function

    def get_content(self, driver: WebDriver):
        self.navigate: bool = not (driver.current_url == self.url)
        
        if self.navigate:
            driver.get(self.url)
        
        self.special_function(driver)

        element: WebElement = driver.find_element(
            by=self.by_attr, value=self.attr_value)

        return self.dict_key, element.text


class WebSite:
    """ Contains multiple WebContent, you can just run WebPage.check() and it returns the content defined in a dict """

    def __init__(self, contents: list[WebContent]) -> None:
        self.contents: list[WebContent] = contents

    def check(self, driver):
        self._dict = {}
        for content_check in self.contents:
            key, value = content_check.get_content(driver)
            self._dict[key] = value
        return self._dict

if __name__ == "__main__":
    print("Not Implimented.")

