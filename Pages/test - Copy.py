import time

import pandas as pd


def read_file(filepath):
    colnames = ["Cat_Name", "Status"]
    # df = pd.read_csv(filepath, sep=',', error_bad_lines=False, index_col=False,  encoding="latin-1")
    df = pd.read_csv(filepath, names=colnames, skiprows=[0], encoding="latin-1", low_memory=False)
    # mean_usage_b = df.memory_usage(deep=True).mean()
    # mean_usage_mb = mean_usage_b / 1024 ** 2
    pd.options.display.max_colwidth = 100000
    return df


rf = read_file("../Pages/mmmm/category with Predictions.csv")
cat_name = rf.Cat_Name.tolist()
time.sleep(2)
status = rf.Status.tolist()
time.sleep(2)

rf1 = read_file('../Pages/mmmm/category_list_after_modelrun.csv')
cat_name1 = rf1.Cat_Name.tolist()

with open('../Pages/mmmm/category_list_after_modelrun.csv', 'r+', encoding="latin-1") as mfile:
    mdata = mfile.read()
    for i in range(0, len(cat_name)):
        chng_word = "__"+str(cat_name[i])+"__"
        chang_status = str(status[i])
        mdata = mdata.replace(chng_word, chang_status)
        print("processing " + str(i))
        # time.sleep(0.5)

    time.sleep(3)

with open('../Pages/mmmm/vab.csv', 'w+', encoding="latin-1") as wfile:
    print(str(len(cat_name1)) + " products are changes")
    wfile.write(mdata)
    time.sleep(2)

# outfile = open('../Pages/mmmm/1.csv', 'w+', encoding="latin-1")
# outfile.write(mdata)
# outfile.close()

time.sleep(3)

# with open('../Pages/mmmm/vab1.csv', 'a+', encoding="latin-1") as mmfile:
#     for i in range(0, len(cat_name1)):
#         mmfile.write("," + str(cat_name1[i]) + "\n")
#         mmfile.write(str(cat_name1[i]) + "\n")

# with open('../Pages/mmmm/vab.csv', 'w+', encoding="latin-1") as wfile:
#     print(str(len(cat_name1)) + " products are changes")
#     wfile.write(mdata)
#     mfile.close()

newrf = read_file('../Pages/mmmm/vab.csv')
cat_name1 = newrf.Cat_Name.tolist()
