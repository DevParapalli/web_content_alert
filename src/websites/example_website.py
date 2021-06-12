from helpers import By, Keys
from website import WebContent, WebSite, WebDriver, WebElement

def special_function(driver: WebDriver):
    """ Intentionally left blank """
    pass

wc1 = WebContent(
        url="http://127.0.0.1:5000/boop",
        by_attr=By.TAG_NAME,
        attr_value="p",
        dict_key="time-text",
        special_function=special_function
    )
    
wc2 = WebContent(
        url="https://example.com",
        by_attr=By.TAG_NAME,
        attr_value="h1",
        dict_key="page-heading",
        special_function=special_function
    )

ws = WebSite(
        [
            wc1,
            #wc2
        ]
    )
    # Its recommended to space the values like this so you can
    # disable individual check by just adding a pound symbol in front of it




EXPORTS = {
    'name':"example-website",
    'type':'website',
    'website': ws
}