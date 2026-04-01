import codecs
import logging
import random
import sys
# import time
from random import randint
from time import sleep
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import asyncio
from BackgroundFunctions.loadObjFile import config_parser
from BackgroundFunctions.readFileData import getURL_List
from fake_useragent import UserAgent

config = config_parser()


class Scraper:
    def __init__(self):
        self.robot = None

    def getWebDriver(self):
        try:
            self.robot = '//*[contains(text(),"To proceed, please verify that you are not a robot.")]'
            opt = Options()
            opt.add_experimental_option("excludeSwitches", ["enable-automation"])
            opt.add_experimental_option("useAutomationExtension", False)
            opt.add_argument("--disable-blink-features=AutomationControlled")
            # opt.add_argument("--disable-extensions")
            opt.add_argument("start-maximized")
            # opt.add_argument('--ignore-ssl-errors=yes')
            # opt.add_argument('--ignore-certificate-errors')
            # opt.add_argument("--disable-javascript")
            # options.add_argument('--headless')
            opt.add_argument('use-fake-ui-for-media-stream')
            # opt.add_argument("window-size=900,1080")
            # opt.add_argument('window-size=1920x1080')
            opt.add_argument("--no-sandbox")
            # opt.add_argument("disable-infobars")
            # opt.add_argument("--disable-dev-shm-usage")
            # opt.add_argument("--disable-gpu")
            # opt.add_experimental_option("excludeSwitches", ["enable-automation"])
            # opt.add_experimental_option("useAutomationExtension", False)
            # opt.add_argument("--disable-blink-features=AutomationControlled")
            # opt.add_argument("start-maximized")
            # opt.add_argument('--disable-popup-blocking')
            # opt.add_argument("--disable-extensions")
            # opt.add_argument("--no-sandbox")
            # opt.add_argument("disable-infobars")
            # opt.add_argument("--disable-dev-shm-usage")
            # opt.add_argument("--disable-javascript")

            # Step 3: Rotate user agents
            # custom_user_agents = [
            #     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            # ]
            #
            # # Select a random user agent
            # custom_user_agent = random.choice(custom_user_agents)
            #
            # # Pass in the selected user agent as an argument
            # opt.add_argument(f'user-agent={custom_user_agent}')

            # opt.add_argument("--disable-gpu")
            drv = webdriver.Remote(command_executor=f"https://dev-selenium-grid.katapult.com/wd/hub", options=opt)
            drv.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")



                # desired_capabilities=DesiredCapabilities.CHROME,
            # drv.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            # drv.delete_all_cookies()
            # stealth(drv, languages=["en-US", "en"],
            #         vendor="Google Inc.",
            #         platform="Win32",
            #         webgl_vendor="Intel Inc.",
            #         renderer="Intel Iris OpenGL Engine",
            #         fix_hairline=True,)
        except Exception as e:
            logging.error(f"Error initializing driver: {e}")
            print("Error initializing driver.")
            sys.exit(1)
        return drv

    # try:
    #     serv = Service(config['filePath']['chromeDriver'])
    #     # Avoiding detection
    #     options = Options()
    #     # Screen resolution set to minimum, maximize screen is one of pattern identified by the bot
    #     options.add_argument("window-size=1536,664")
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--disable-dev-shm-usage")
    #
    #     # Chrome is controlled by automated test software
    #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #     options.add_experimental_option('useAutomationExtension', False)
    #     options.add_argument('--disable-blink-features=AutomationControlled')
    #     # options.add_argument('--disable-gpu')
    #     # Initiate user agent with webdeiver
    #     user_agent = UserAgent()
    #     user_agent = user_agent.random
    #     print(user_agent)
    #     # options.add_argument(f'user-agent={user_agent}')
    #     # options.add_argument(
    #     #     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '
    #     #     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Mobile Safari/537.36 Edge/12.10166"')
    #     driver = webdriver.Chrome(service=serv, options=options)
    #     # Selenium Stealth settings
    #     stealth(driver,
    #             languages=["en-US", "en"],
    #             vendor="Google Inc.",
    #             platform="Win32",
    #             webgl_vendor="Intel Inc.",
    #             renderer="Intel Iris OpenGL Engine",
    #             fix_hairline=True,
    #             )
    #     return driver
    # except Exception as e:
    #     logging.error(f"Error initializing driver: {e}")
    #     print("Error initializing driver.")
    #     sys.exit(1)

    # drv.refresh()
    # drv.maximize_window()


getobj = Scraper()


def save_page_data():
    drv = getobj.getWebDriver()
    get_url_link = getURL_List()

    for posts in range(len(get_url_link)):
        print(posts+1)
        # drv.delete_all_cookies()
        # drv.get(get_url_link[posts])
        # input("Press enter button")
        # await asyncio.sleep(10, "drv.get(get_url_link[posts])")
        # drv.refresh()
        # sleep(1.7)
        drv.get(get_url_link[posts])
        sleep(1.6)
        if posts == 0:
            input("Press enter button")
            ff = open(config['filePath']['html_file_name'] + str(posts) + '.html', 'w')
            ff.close()
            # open file in write mode with encoding
            f = codecs.open(config['filePath']['html_file_name'] + str(posts) + '.html', "r+", "utf8")
            # obtain page source
            h = drv.page_source
            # write page source content to file
            f.write(h)
            print("Page " + str(posts + 1) + " Saved")
        else:
            # print("hello")
            ff = open(config['filePath']['html_file_name'] + str(posts) + '.html', 'w')
            ff.close()
            # open file in write mode with encoding
            f = codecs.open(config['filePath']['html_file_name'] + str(posts) + '.html', "r+", "utf8")
            # obtain page source
            h = drv.page_source
            # write page source content to file
            f.write(h)
            print("Page " + str(posts + 1) + " Saved")
            continue
        # ff = open(config['filePath']['html_file_name'] + str(posts) + '.html', 'w')
        # ff.close()
        # # open file in write mode with encoding
        # f = codecs.open(config['filePath']['html_file_name'] + str(posts) + '.html', "r+", "utf8")
        # # obtain page source
        # h = drv.page_source
        # # write page source content to file
        # f.write(h)
        # print("Page " + str(posts + 1) + " Saved")
        sleep(1)
        # drv.delete_all_cookies()
        chwd = drv.window_handles
        current_tab = drv.current_window_handle
        for window in chwd:
            if window != current_tab:
                drv.switch_to.window(window)
                print("Closing Tab = " + drv.title)
                # close() method is used to close the selected tab.
                drv.close()
                # sleep(1.5)
            else:
                print("Vaibhav")
                continue
    drv.quit()
    # sleep(1.5)

    # for i in range(0, len(get_url_link)):
    #     sleep(3.5)
    #     # drv.delete_all_cookies()
    #     # drv.delete_network_conditions()
    #     for posts in range(len(get_url_link)):
    #         print(posts)
    #         drv.get(get_url_link[posts])
    #         input("Press enter button")
    #         ff = open(config['filePath']['html_file_name'] + str(posts) + '.html', 'w')
    #         ff.close()
    #         # open file in write mode with encoding
    #         f = codecs.open(config['filePath']['html_file_name'] + str(posts) + '.html', "r+", "utf8")
    #         # obtain page source
    #         h = drv.page_source
    #         # write page source content to file
    #         f.write(h)
    #         sleep(3.5)
    #         print("Page " + str(i + 1) + " Saved")
    #         sleep(randint(3, 5))
    #         if posts != len(get_url_link) - 1:
    #             drv.execute_script("window.open('');")
    #             chwd = drv.window_handles
    #             drv.switch_to.window(chwd[-1])
    #     chwd = drv.window_handles
    #     print(chwd)
    #     # drv.get(get_url_link[i])
    #     # input("Press enter button")
    #     # drv.refresh()
    #     # sleep(4.5)
    #     # ff = open(config['filePath']['html_file_name'] + str(i) + '.html', 'w')
    #     # ff.close()
    #     # # open file in write mode with encoding
    #     # f = codecs.open(config['filePath']['html_file_name'] + str(i) + '.html', "r+", "utf8")
    #     # # obtain page source
    #     # h = drv.page_source
    #     # # write page source content to file
    #     # f.write(h)
    #     # sleep(3.5)
    #     # print("Page " + str(i + 1) + " Saved")
    #     # sleep(randint(3, 5))

