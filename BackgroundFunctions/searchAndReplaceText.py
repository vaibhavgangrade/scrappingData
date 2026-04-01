import time
import pandas as pd

from BackgroundFunctions.deleteFiles import delete_files
from BackgroundFunctions.readFileData import config
from Pages.getProdcutNames import get_ProductNames


class FindandReplace:
    new_file = open(config["filePath"]["newresultfile"], "a", encoding="utf8")

    def search_replace(self):
        get_ProductNames()
        search_text = [
            "||",
            " alt=",
            '"',
            ", ",
            "  ",
            "\t\t",
            "\n\n",
            "\t\t\t\t\t\t\t\t",
            "\t",
            " >",
            "a-color-base a-text-normal",
            "\n ",
            ">",
        ]
        replace_text = ["\n", " ", "", "\t", "\t\t"]
        # Opening our text file in read only
        # mode using the open() function
        with open(config["filePath"]["resultfile"], "r+", encoding="utf8") as rfile:
            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            data = rfile.read()

            # Searching and replacing the text
            # using the replace() function
            data = data.replace(search_text[0], replace_text[0])
            data = data.replace(search_text[1], replace_text[2])
            data = data.replace(search_text[7], replace_text[4])
            data = data.replace(search_text[2], replace_text[2])
            data = data.replace(search_text[3], replace_text[1])
            data = data.replace(search_text[5], replace_text[2])
            data = data.replace(search_text[6], replace_text[0])
            data = data.replace(search_text[8], replace_text[0])
            data = data.replace(search_text[10], replace_text[1])
            data = data.replace(search_text[9], replace_text[0])
            data = data.replace(search_text[11], replace_text[0])
            data = data.replace(search_text[4], replace_text[1])
            data = data.replace(search_text[4], replace_text[1])
            data = data.replace(search_text[1], replace_text[2])
            data = data.replace(search_text[4], replace_text[1])
            data = data.replace(search_text[4], replace_text[1])
            data = data.replace(search_text[2], replace_text[2])
            data = data.replace(search_text[2], replace_text[2])
            # data = data.replace(search_text[13], replace_text[5])
            data = data.replace(search_text[12], replace_text[2])
            return data

    def writeTofile(self):
        myobj = FindandReplace()
        test = myobj.search_replace()
        time.sleep(3)
        column_names = ["Category_Names", "Product_Names"]
        with open(config["filePath"]["newresultfile"], "w", encoding="utf8") as wfile:
            wfile.write(test)
            wfile.close()
        myobj.write_to_csv()

    def write_to_csv(self):
        with open(config["filePath"]["outputfile"], "a", encoding="utf8") as csvfile:
            csvfile.close()
            column_names = ["Category_Names", "Product_Names"]
            df = pd.read_csv(
                config["filePath"]["newresultfile"],
                names=column_names,
                on_bad_lines="skip",
            )  # , names=column_names, on_bad_lines='skip'
            df.to_csv(
                config["filePath"]["outputfile"], mode="a", index=False, header=False
            )

        # time.sleep(1)
        # delete_files()

    # def final_del_file(self):
    #     delete_files()