import os
import time

from Pages.getProdcutNames import get_url_link, config


def fileToDelete(filenames):
    if os.path.isfile(filenames):
        os.remove(filenames)
        print("---------------------- " + filenames + " File Removed----------------")
    else:
        # If it fails, inform the user.
        print("Error: %s file not found" % filenames)


def delete_files():
    for i in range(0, len(get_url_link)):
        fileToDelete(config['filePath']['html_file_name'] + str(i) + '.html')
        print("file " + config['filePath']['html_file_name'] + str(i) + '.html' + " deleted successfully")
    time.sleep(3)
    fileToDelete(config['filePath']['resultfile'])
    time.sleep(2)
    fileToDelete(config['filePath']['newresultfile'])
