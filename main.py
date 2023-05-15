import data_loader as dl


def main():


    data = dl.load_enertalk(R'data\enertalk\20161002\03_washing-machine.parquet.gzip')
    data['active_power'] = dl.filter_data(data['active_power'], 300)
    dl.plot_enertalk(data, "fridge", '20161002')


if __name__ == '__main__':
    main()
