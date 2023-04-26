import data_loader as dl

def main():
    # here R before the string marks it as 'raw', so it interprets \t as a text
    data = dl.load(R'data\tracebase-master\complete\Refrigerator\dev_76C07F_2012.06.19.csv')
    dl.plot(data)


if __name__ == '__main__':
    main()