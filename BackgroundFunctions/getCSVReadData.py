import csv

from selenium import webdriver


class Test:
    def readCSVFile(self, filename):
        urls = []
        titles = []

        with open(filename) as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            for row in csvReader:
                urls.append(row['URL'])
                titles.append(row['title'])

        return dict(zip(urls, titles))

    def test_read_csv_file(self):
        testObject = Test()
        pages = testObject.readCSVFile("D:PATHfile-with-header.csv")
        self.driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
        print(pages)
        for url, title in pages.items():
            print(url)
            self.driver.get(url)
            self.assertEqual(title, self.driver.title, "title is not matching")
