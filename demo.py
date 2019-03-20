from learn.cluster import cluster
from learn.regress import regress

# Cluster sale codes and group by cluster.
# Sale codes in demo clusters are printed to be used in Looker to 
# find the best selling products in each cluster.
# Looker queries had to be done manually :(

# These are the clusters the demo stores fall in (out of 100)
DEMO_CLUSTER_1 = 21
DEMO_CLUSTER_2 = 88
DEMO_CLUSTER_3 = 44

def demo():
    # create and fit cluster model (cluster stores)
    sale_codes, X, y = cluster()
    # create and fit regress model (to predict what cluster a store belongs to)
    regress(X, y)
    # build [sale_code, cluster_no ] list
    sale_code_cluster = []
    for i in range(len(sale_codes)):
        sale_code_cluster.append([sale_codes[i], y[i]])
    # sort by cluster_no
    sale_code_cluster.sort(key=lambda x: x[1])
    # divide into cluster groups 
    sale_code_groups = []
    sale_code_group = []
    for i in range(len(sale_code_cluster)):
        sale_code_group.append(sale_code_cluster[i][0])
        if i == len(sale_code_cluster) - 1:
           sale_code_groups.append(sale_code_group)
           break 
        if (sale_code_cluster[i][1] != sale_code_cluster[i+1][1]):
            sale_code_groups.append(sale_code_group)
            sale_code_group = []
    # print clusters that demo stores belong to
    for i in range(len(sale_code_groups)):
        if i == DEMO_CLUSTER_1 or i == DEMO_CLUSTER_2 or i == DEMO_CLUSTER_3:
            print(sale_code_groups[i])
            print("\n\n\n")
  
if __name__ == '__main__':
    demo()