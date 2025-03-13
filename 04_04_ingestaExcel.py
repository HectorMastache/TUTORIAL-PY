import pandas

if __name__ == '__main__':

    # LEEMOS ARCHIVO EN EXCEL
    df = pandas.read_excel('DataMeterCCJanuary.xlsx')

    print(df.head()) 
    print(df.info())
    print(df.describe())
