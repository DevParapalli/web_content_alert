from util import EXPORTS as UTIL
from selenium import webdriver
from datetime import datetime

# Driver Definitions
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# Change to whatever browser you have or something.
remote_driver = webdriver.Chrome(options=options)

# Driver should have finished setup until now
alerts = {}
websites = {}
endpoints = {}

# get_state
# We will use only 1 store
store = UTIL['stores'][0].EXPORTS['store']
previous_state = store.get_state()
try:
    previous_websites = previous_state['websites']
    previous_endpoints = previous_state['endpoints']
except KeyError: # Incase of timeout
    previous_websites = {}
    previous_endpoints = {}

for website in UTIL['websites']:
    websites[website] = UTIL['websites'][website].EXPORTS['website'].check(remote_driver)

for alert in UTIL['alerts']:
    alerts[alert] = UTIL['alerts'][alert].EXPORTS['alert-function'].execute

for endpoint in UTIL['endpoints']:
    endpoints[endpoint] = UTIL['endpoints'][endpoint].EXPORTS['endpoint'].get_data()

def mass_alert(title, message):
    for alert in alerts:
        alerts[alert](title, message)

mass_alert(
    f"STATUS",
    f"Started Checks at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)


for website in websites:
    if website not in previous_websites:
        #If the site wasn't tracked before.
        # Send alert informing for new tracker
        mass_alert(
            f"{website}",
            f"Tracking New Site: {website}, with params {[key for key in websites[website]]}"
        )
        #Report with current values.
        for key in websites[website]:
            mass_alert(
                f"{website}",
                f"NEW KEY ADDED: {key}, \nNow: {websites[website][key]}"
            )
        # We skip the rest of the loop because we have no data for comparision.
        continue

    # This part runs if site is tracked
    for key in websites[website]:
        if key in previous_websites[website]:
            # We check if we previously tracked this key
            if not websites[website][key] == previous_websites[website][key]:
                # If tracked, is the value similar to before ? if not, send alert
                mass_alert(
                    f"{website}",
                    f"CHANGE DETECTED\nKey:{key}\nPreviously: {previous_websites[website][key]} \nNow: {websites[website][key]}"
                )
        else:
            # We didn't track this key
            mass_alert(
                f"{website}",
                f"NEW KEY ADDED: {key} \nNow: {websites[website][key]}"
            )

for website in previous_websites:
    if website not in websites:
        # If site isn't present in current state but was previously tracked.
        mass_alert(
            f"{website}",
            f"REMOVED TRACKING FOR {website}."
        )


remote_driver.close()

# LOGIC FOR ENDPOINTS

for endpoint in endpoints:
    if endpoint not in previous_endpoints:
        #If the site wasn't tracked before.
        # Send alert informing for new tracker
        mass_alert(
            f"{endpoint}",
            f"Tracking New Endpoint: {endpoint}, with params {[key for key in endpoints[endpoint]]}"
        )
        #Report with current values.
        for key in endpoints[endpoint]:
            mass_alert(
                f"{endpoint}",
                f"NEW KEY ADDED: {key}, \nNow: {endpoints[endpoint][key]}"
            )
        # We skip the rest of the loop because we have no data for comparision.
        continue

    # This part runs if site is tracked
    for key in endpoints[endpoint]:
        if key in previous_endpoints[endpoint]:
            # We check if we previously tracked this key
            if not endpoints[endpoint][key] == previous_endpoints[endpoint][key]:
                # If tracked, is the value similar to before ? if not, send alert
                mass_alert(
                    f"{endpoint}",
                    f"CHANGE DETECTED\nKey:{key}\nPreviously: {previous_endpoints[endpoint][key]} \nNow: {endpoints[endpoint][key]}"
                )
        else:
            # We didn't track this key
            mass_alert(
                f"{endpoint}",
                f"NEW KEY ADDED: {key}, \nNow: {endpoints[endpoint][key]}"
            )

for endpoint in previous_endpoints:
    if endpoint not in endpoints:
        # If site isn't present in current state but was previously tracked.
        mass_alert(
            f"{endpoint}",
            f"REMOVED TRACKING FOR {endpoint}."
        )

store.store_state(
    {
        "websites":websites,
        "endpoints":endpoints
    }
)



mass_alert(
    "STATUS",
    f"Ended Checks at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)