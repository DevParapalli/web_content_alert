from util import EXPORTS
from selenium import webdriver


# Driver Definitions
options = webdriver.ChromeOptions()
options.add_argument('--headless')
remote_driver = webdriver.Chrome(options=options) # Change to whatever browser you have or something.

# Driver should have finished setup until now 
alerts = {}
websites = {}

# get_state
# We will use only 1 store 
store = EXPORTS['stores'][0].EXPORTS['store']
previous_state = store.get_state()

for website in EXPORTS['websites']:
    websites[website] = EXPORTS['websites'][website].EXPORTS['website'].check(remote_driver)

for alert in EXPORTS['alerts']:
    alerts[alert] = EXPORTS['alerts'][alert].EXPORTS['alert-function'].execute

def mass_alert(title, message):
    for alert in alerts:
        alerts[alert](title, message)

for website in websites:
    if website not in previous_state:
        mass_alert(
            f"{website}",
            f"Tracking New Site: {website}, with params {[key for key in websites[website]]}"
        )
        continue
    for key in websites[website]:
        if key in previous_state[website]:
            if not websites[website][key] == previous_state[website][key]:
                mass_alert(
                    f"{website}",
                    f"CHANGE\nKey:{key}\nPreviously: {previous_state[website][key]} \nNow: {websites[website][key]}"
                )
        else:
            mass_alert(
                f"{website}",
                f"NEW KEY ADDED: {key}, \nNow: {websites[website][key]}"
            )

store.store_state(websites)



remote_driver.close()