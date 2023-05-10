import data_loader as dl

def main():
    # here R before the string marks it as 'raw', so it interprets \t as a text
    csv_files = [R'data\tracebase-master\complete\Refrigerator\dev_599393_2012.01.20.csv', R'data\tracebase-master\complete\MicrowaveOven\dev_98A0D3_2011.09.19.csv']
    
    data = dl.load(R'data\tracebase-master\complete\MicrowaveOven\dev_98A0D3_2011.09.19.csv')
    dl.plot(data)
    dl.plot_aggregated(dl.sum_power_values2(csv_files))

    # dl.plot(data)
    print('done')

if __name__ == '__main__':
    main()