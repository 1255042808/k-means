def read_20180829():
    fname = "20180829.xlsx"
    bk = xlrd.open_workbook(fname)
    # shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print("no sheet in %s named Sheet1" % fname)
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    # 获取第一行第一列数据
    cell_value = sh.cell_value(1, 0)
    time = []
    single1 = []
    single2 = []
    single3 = []
    # 获取各行数据
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 0)
        time.append(row_data)
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 1)
        single1.append(row_data)
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 2)
        single2.append(row_data)
    for i in range(1, nrows):
        row_data = sh.cell_value(i, 3)
        single3.append(row_data)
    return time,single1,single2,single3
