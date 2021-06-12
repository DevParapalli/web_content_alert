import pkgutil, importlib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

# Finding out all installed alerts and websites
alerts = [name for _, name, _ in pkgutil.iter_modules([f"{BASE_DIR / 'alerts'}"])]
websites = [name for _, name, _ in pkgutil.iter_modules([f"{BASE_DIR / 'websites'}"])]
endpoints = [name for _, name, _ in pkgutil.iter_modules([f"{BASE_DIR / 'endpoints'}"])]
stores = [name for _, name, _ in pkgutil.iter_modules([f"{BASE_DIR / 'stores'}"])]

def alert_importer(alert):
    return importlib.import_module(f'alerts.{alert}')

def website_importer(website):
    return importlib.import_module(f'websites.{website}')

def endpoint_importer(endpoint):
    return importlib.import_module(f'endpoints.{endpoint}')

def store_importer(store):
    return importlib.import_module(f'stores.{store}')

# Removing examples.
alerts.pop(alerts.index('example_alert'))
#websites.pop(websites.index('example_website'))
endpoints.pop(endpoints.index('example_endpoint'))
stores.pop(stores.index('example_store'))


EXPORTS = {
    'alerts':{},
    'websites':{},
    'stores':[],
    'endpoints':{}

}

for alert in alerts:
    EXPORTS['alerts'][alert] = alert_importer(alert)

for website in websites:
    EXPORTS['websites'][website] = website_importer(website)

for endpoint in endpoints:
    EXPORTS['endpoints'][endpoint] = endpoint_importer(endpoint)

for store in stores:
    EXPORTS['stores'].append(store_importer(store))

