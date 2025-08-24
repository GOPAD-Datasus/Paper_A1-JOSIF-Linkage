from linkage import link, preprocess


if __name__ == '__main__':
    sinasc, sim = preprocess()
    link(sinasc, sim)
