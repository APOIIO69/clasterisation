from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as pl
from sklearn.cluster import KMeans

from creating_datasets import return_lst_of_frames
from dendrogramm_writer import return_dataframe


def build_dendrogram():
    link = linkage(return_dataframe(return_lst_of_frames()[7][0]), 'ward')
    dn = dendrogram(link)
    pl.savefig("data/dendrograms/dendrogram_7.jpg")


def build_elbow():
    for frame, _ in return_lst_of_frames():
        df = return_dataframe(frame)
        k = range(1, 10)
        models = [KMeans(n_clusters=i, random_state=42).fit(df) for i in k]
        dist = [model.inertia_ for model in models]
        pl.plot(k, dist, marker='o')
        pl.xlabel('k')
        pl.ylabel('sum of distances')
        pl.title('The Elbow Method')
        pl.savefig(f'elbow_method_{frame}.jpg')


def count_clusters():
    for i in range(len(return_lst_of_frames())):
        df = return_dataframe(return_lst_of_frames()[i][0])
        link = linkage(df, 'ward')
        df['cluster_alg'] = fcluster(link, 3, criterion='maxclust')
        print(df.groupby('cluster_alg').size())


def build_k_means_model():
    for frame, _ in return_lst_of_frames():
        df = return_dataframe(frame)
        model = KMeans(n_clusters=3, random_state=42)
        model.fit(df)
        df['cluster_km'] = model.labels_
        print(df.groupby('cluster_km').size())
