import data_loader as dl

def main():
    # here R before the string marks it as 'raw', so it interprets \t as a text
    data = dl.load(R'data\tracebase-master\complete\Lamp\_D3237E_2012.01.11.csv')
    dl.plot(data)


if __name__ == '__main__':
    main()