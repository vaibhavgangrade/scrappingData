import re
import time

from BackgroundFunctions.loadObjFile import config_parser
from BackgroundFunctions.readFileData import getURL_List, write_file, read_file
from Pages.getPageSource import save_page_data
from datetime import datetime

get_url_link = getURL_List()
config = config_parser()

save_data = open(config['filePath']['resultfile'], 'a', encoding="utf-8")

final_data = open(config['filePath']['final_file'], 'a', encoding="utf-8")


def get_ProductNames():
    startTime = datetime.now()
    print(str(startTime))
    save_page_data()
    time.sleep(2)
    category_regex = config['regex']['abt_cat']
    title_regex = config['regex']['target_title']
    title_regex2 = config['regex']['zales_title1']
    product_regex = config['regex']['abt_prd']
    # save_data.write("Category_Name" + ',' + "Product_Name" + "\n")
    print(len(get_url_link))
    for count in range(0, len(get_url_link)):
        cat_file_name = open(config['filePath']['html_file_name'] + str(count) + '.html', "r+", encoding="utf8")
        cat_match = re.findall(category_regex, cat_file_name.read())
        product_file_name = open(config['filePath']['html_file_name'] + str(count) + '.html', "r+", encoding="utf8")
        prod_match = re.findall(product_regex, product_file_name.read())
        title_file_name = open(config['filePath']['html_file_name'] + str(count) + '.html', "r+", encoding="utf8")
        title_match = re.findall(title_regex, title_file_name.read())
        # print(cat_match)
        newcat_name = ""
        print("page " + str(count))

        for ls in cat_match:
            newcat_name += ls + "/"
            # print(newcat_name)
        # if len(title_match) != 0:
        #     for title in title_match:
        #         newcat_name += title
        # else:
        #     print("sorry no title")
        # print("newcat_name after change", newcat_name)

        if cat_match is not None:
            for prd_name in prod_match:
                # prd_name_repl1 = prd_name[count].replace("   ", " ")
                # prd_name_final = prd_name_repl1.replace(",", " ")
                # prd_name_final2 = prd_name_final.replace("' tireModel: '", " ")
                cat_name_repl = newcat_name.replace(",", " ")
                cat_name_2 = cat_name_repl.replace(" \\u003E ", "/")
                cat_name_repl_final = cat_name_2.replace("  ", " ")

                # prd_name[:prd_name.rfind(',')].replace(',', '') + prd_name[prd_name.rfind(','):]
                save_data.write(str(prd_name) + ',' + str(cat_name_repl_final) + "\n")

            print("From file extracted products " + str(len(prod_match)))

        else:
            print("No category and product names are found")
            break
    print("Process finished in ", str(datetime.now() - startTime))

    # if newcat_name is not None:
    #     for prd_name in prod_match:
    #         mystring = prd_name.replace(",", " ")
    #         mystring2 = mystring.replace("  ", " ")
    #         save_data.write(newcat_name + ',' + str(mystring2) + "\n")
    #
    #     print("From file extracted products " + str(len(prod_match)))
    #
    # else:
    #     print("No category and product names are found")
    # break
    # for cat_name in cat_match:
    #     newcat_name = str(cat_name) + " /"
    #     for prd_name in prod_match:
    #         mystring = prd_name.replace(",", " ")
    #         mystring2 = mystring.replace("  ", " ")
    #
    #
    #         # prd_name[:prd_name.rfind(',')].replace(',', '') + prd_name[prd_name.rfind(','):]

    # if cat_match is not None:
    #     for cat_name in cat_match:
    #         newcat_name = str(cat_name) + " /"
    #         for prd_name in prod_match:
    #             mystring = prd_name.replace(",", " ")
    #             mystring2 = mystring.replace("  ", " ")
    #
    #
    #             # prd_name[:prd_name.rfind(',')].replace(',', '') + prd_name[prd_name.rfind(','):]
    #             save_data.write(newcat_name + ',' + str(mystring2) + "\n")
    #
    #         print("From file extracted products " + str(len(prod_match)))
    #
    # else:
    #     print("No category and product names are found")
    #     break

    save_data.close()
