import data_loader as dl

def main():
    # here R before the string marks it as 'raw', so it interprets \t as a text
    # data = dl.load(R'data\tracebase-master\complete\TV-LCD\dev_B80E51_2012.05.15.csv')
    # data = dl.load(R'data\tracebase-master\complete\Printer\dev_11F01E_2011.12.26.csv')
    data = dl.load(R'data\tracebase-master\complete\Refrigerator\dev_98C08A_2011.08.09.csv')
    # data = dl.load(R'data\tracebase-master\complete\LaundryDryer\_D36122_2012.01.24.csv')
    csv_files = [R'data\tracebase-master\complete\Refrigerator\dev_599393_2012.01.20.csv', R'data\tracebase-master\complete\Lamp\dev_D331DA_2012.01.20.csv']
    output_file = '2012.01.20.csv'
    dl.sum_power_values(csv_files, output_file)

    # dl.plot(data)


if __name__ == '__main__':
    main()