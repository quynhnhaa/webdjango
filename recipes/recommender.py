import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcooking.settings")

django.setup()
# ------------------------------------------------------------------------------------------------------------

from reviews.models import Review
import pandas as pd
import pandas as pd 
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse 

class CF(object):
    def __init__(self, Y_data, K=10, dist_fun=cosine_similarity, uuCF=1):
        self.uuCF = uuCF
        self.Y_data = Y_data if uuCF else Y_data[:, [1, 0, 2]]
        self.K = K
        self.dist_fun = dist_fun
        self.Ybar_data = None

        self.n_users = int(np.max(Y_data[:, 0])) + 1
        self.n_items = int(np.max(Y_data[:, 1])) + 1
    def add(self, new_data):
        self.Y_data = np.concatenate((self.Y_data, new_data), axis=0)
        self.n_users = int(np.max(self.Y_data[:, 0])) + 1
        self.n_items = int(np.max(self.Y_data[:, 1])) + 1

    def normalize_Y(self):
        users = self.Y_data[:, 0]
        self.Ybar_data = self.Y_data.copy()
        self.mu = np.zeros((self.n_users))
        for n in range(self.n_users):
            ids = np.where(users == n)[0]
            ratings = self.Y_data[ids, 2].astype(np.float32)

            if ratings.size > 0:
                m = ratings.mean()
            else:
                m = 0
            self.mu[n] = m

            self.Ybar_data[ids, 2] = ratings - self.mu[n]
        self.Ybar_data = np.array(self.Ybar_data, dtype=np.float64)
        # print(self.Ybar_data)
    
        #Transform the data into a matrix
        self.Ybar = sparse.coo_matrix((self.Ybar_data[:,2], (self.Ybar_data[:, 1], self.Ybar_data[:, 0] )), (self.n_items, self.n_users))
        self.Ybar = self.Ybar.tocsr()
        # print(self.Ybar)

    def similarity(self):
        self.S = self.dist_fun(self.Ybar.T, self.Ybar.T)

    def refresh(self):
        self.normalize_Y()
        self.similarity()
    
    def fit(self):
        self.refresh()

    def __pred(self, u, i, normalized=1):
        ids = np.where(self.Y_data[:,1] == i)[0].astype(np.int32)
        users_rated_i = self.Y_data[ids, 0].astype(np.int32)

        sim = self.S[u, users_rated_i]
    
        a= np.argsort(sim)[-self.K:]
        nearest_r = sim[a]
        r = self.Ybar[i, users_rated_i[a]]

        if normalized:
            return (r*nearest_r).sum() / (np.abs(nearest_r.sum()) + 1e-8)
        return (r*nearest_r).sum() / (np.abs(nearest_r.sum()) + 1e-8) + self.mu[u]
    
    def pred(self, u, i, normalized = 1):
        if self.uuCF: return self.__pred(u, i, normalized)
        return self.__pred(i, u, normalized)

    def recommend(self, u):
        ids = np.where(self.Y_data[:, 0] == u)[0].astype(np.int32)
        rated_items_by_u = self.Y_data[ids, 1].astype(np.int32)
        recommended_items = []
        for i in range(self.n_items):
            if i not in rated_items_by_u:
                ratings = self.__pred(u,i)
                recommended_items.append([i,ratings])
        return recommended_items
    
    def print_recommendation(self):
        print('Recommendation:')
        for u in range(self.n_users):
            recommended_items = self.recommend(u)

            # Sắp xếp theo điểm dự đoán giảm dần và lọc > 0
            top_items = sorted(
                [(item, round(score, 2)) for item, score in recommended_items if score > 0],
                key=lambda x: x[1],
                reverse=True
            )[:10]  # Lấy top 10

            if self.uuCF:
                print(f'  User {u} => Top 10 recommend items:', end=' ')
            else:
                print(f'  Item {u} => Recommend to top 10 users:', end=' ')

            if top_items:
                print(", ".join(f"[{item}, {score}]" for item, score in top_items))
            else:
                print("Không có đề xuất phù hợp.")


    
if __name__ == '__main__':
    reviews = Review.objects.all().values()
    Y_data = np.array([[r.get('user_id'), r.get("recipe_id"), r.get("rating")] for r in reviews])
    cf = CF(Y_data, uuCF=1)
    cf.fit()
    # cf.Ybar_data[:2]
    cf.print_recommendation()