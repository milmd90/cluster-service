from cluster import cluster
from regress import regress

def learn():
    X, y = cluster()
    regress(X, y)

if __name__ == '__main__':
    learn()