from linkage.linkage.linkage import link
from linkage.preprocessing.preprocess import preprocess

if __name__ == '__main__':
    sinasc, sim = preprocess()
    link(sinasc, sim)