import data_loader as dl

def main():
    # here R before the string marks it as 'raw', so it interprets \t as a text
    data = dl.load(R'data\tracebase-master\complete\Amplifier\dev_AF6490_2011.12.28.csv')
    dl.plot(data)


if __name__ == '__main__':
    main()