import codecs
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from BackgroundFunctions.loadObjFile import config_parser
from BackgroundFunctions.readFileData import getURL_List

config = config_parser()
save_data = open(config['filePath']['resultfile'], 'a', encoding="utf8")
new_file = open(config['filePath']['newresultfile'], 'a', encoding='utf8')  # , encoding="utf8"
output_file = open(config['filePath']['outputfile'], 'a', encoding='utf8')  # , encoding="utf8"


def getWebDriver():
    options = FirefoxOptions()
    options.add_argument("--width=1536")
    options.add_argument("--height=664")
    # user_agent = UserAgent()
    # user_agent = user_agent.random
    # print(user_agent)
    # options.add_argument(f'user-agent={user_agent}')
    options.binary_location = r"C:\Users\VaibhavGangrade\AppData\Local\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(firefox_profile=r'C:\Users\VaibhavGangrade\AppData\Roaming\Mozilla\Firefox\Profiles'
                                               r'\23jx84l7.default-release', options=options)

    # serv = Service(config['filePath']['gekoDriver'])
    # driver = webdriver.Firefox()
    # Avoiding detection
    # options = FirefoxOptions()
    # # Screen resolution set to minimum, maximize screen is one of pattern identified by the bot
    # options.add_argument("window-size=1400,600")
    # options.headless = True
    # Chrome is controlled by automated test software
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # options.add_experimental_option('useAutomationExtension', False)
    #
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--disable-gpu')
    # Initiate user agent with webdeiver
    # options.binary_location = r"C:\Users\VaibhavGangrade\AppData\Local\Mozilla Firefox\firefox.exe"
    # user_agent = UserAgent()
    # user_agent = user_agent.random
    # print(user_agent)
    # options.add_argument(f'user-agent={user_agent}')
    # options.add_argument(
    #     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '
    #     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Mobile Safari/537.36 Edge/12.10166"')
    # driver = webdriver.Chrome(service=serv, options=options)
    # driver = webdriver.Firefox(executable_path=r'./FilesDirectory/geckodriver.exe')
    # Selenium Stealth settings
    # stealth(driver,
    #         languages=["en-US", "en"],
    #         vendor="Google Inc.",
    #         platform="Win32",
    #         webgl_vendor="Intel Inc.",
    #         renderer="Intel Iris OpenGL Engine",
    #         fix_hairline=True,
    #         )
    return driver


def save_page_data():
    get_url_link = getURL_List()
    for i in range(0, len(get_url_link)):
        drv = getWebDriver()
        drv.refresh()
        drv.maximize_window()
        # drv.delete_all_cookies()
        sleep(randint(1, 5))
        # drv.delete_network_conditions()
        drv.get(get_url_link[i])
        sleep(randint(3, 5))
        # drv.get(get_url_link[i])
        f1 = open(config['filePath']['html_file_name'] + str(i) + '.html', 'w')
        f1.close()
        # open file in write mode with encoding
        f = codecs.open(config['filePath']['html_file_name'] + str(i) + '.html', "r+", "utf8")
        # obtain page source
        h = drv.page_source
        # sleep(randint(3, 5))
        # write page source content to file
        f.write(h)
        sleep(randint(1, 5))
        print("Page " + str(i + 1) + " Saved")
        drv.close()
        sleep(randint(2, 7))
