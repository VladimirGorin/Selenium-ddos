from utils import create_driver, read_settings
import time
from concurrent.futures import ThreadPoolExecutor

SETTINGS_PATH = "./settings.json"
MAX_THREADS = 5

settings = read_settings(SETTINGS_PATH)

def visit_target(_):
    driver = create_driver()
    driver.get(settings["target"])
    time.sleep(2)
    driver.quit()

with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    executor.map(visit_target, range(settings["visit"]))
