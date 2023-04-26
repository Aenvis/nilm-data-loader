import data_loader as dl

def main():
    # here R before the string marks it as 'raw', so it interprets \t as a text
    data = dl.load(R'data\tracebase-master\complete\Freezer\dev_D36601_2011.12.16.csv')
    dl.plot(data)


if __name__ == '__main__':
    main()