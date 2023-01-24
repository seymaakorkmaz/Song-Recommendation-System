import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from decimal import Decimal

data_set = pd.read_csv("DataSet.csv")  # Pandas kütüphanesi kullanılarak csv dosyası bir dataframe'e okunmuştur.
data_set = data_set.drop_duplicates(subset="Name")  # Veri setindeki tekrar eden veriler temizlenmiştir.
data_set = data_set.drop(['Release_date', 'Length', 'Time Signature'], axis=1)  # Veri setindeki kullanılmayan kolonlar
data_set = data_set.reset_index(drop=True)  # Verileri temizlemenin ardından indexler düzenlenmiştir.

# Dataframe'deki string veriler uppercase yapılarak kullanıcı girdisiyle uyumluluk sağlanmıştır.
data_set['Name'] = data_set['Name'].str.upper()
data_set['Album'] = data_set['Album'].str.upper()
data_set['Artist'] = data_set['Artist'].str.upper()

# Normalize edilecek (nümerik değer içeren) kolonlar seçilmiştir
feature_cols = ['Acousticness', 'Danceability', 'Energy',
                'Instrumentalness', 'Liveness', 'Loudness',
                'Speechiness', 'Tempo', 'Popularity']

scaler = MinMaxScaler()
# Veri normalize edilmiştir.
normalized_df = scaler.fit_transform(data_set[feature_cols])
# Versi setindeki veriler için cosine similarity değerleri hesaplanarak cosine değişkenine atılmıştır.
cosine = cosine_similarity(normalized_df)


# Veri setindeki 'Name' kolonu için generate_Recommendation fonksiyonunda kullanmak üze bir indis dizisi oluşturulmuştur
indices = pd.Series(data_set.index, index=data_set['Name'])
indices.drop_duplicates()


# Kullanıcının girdiği şarkıya yönelik şarkı önerisi yapan fonksiyon
def generate_recommendation(song_title):
    # Girilen şarkının cosine similarity değerleri score dizisine atılır.
    score = list(enumerate(cosine[indices[song_title]]))

    # Score dizisi sort edilerek similarity_score dizisne atılır.
    similarity_score = sorted(score, key=lambda x: x[1], reverse=True)

    # similarity_score dizisindeki top 7 şarkı alınır.
    similarity_score = similarity_score[1:8]

    # Önerilen top 7 şarkının indexleri alınır.
    top_songs_index = [i[0] for i in similarity_score]

    # top 7 şarkı, sanatçı ve cosine similarity değerleri fonksiyondan return edilir.
    top_songs = data_set['Name'].iloc[top_songs_index]
    artists = data_set['Artist'].iloc[top_songs_index]
    return top_songs, artists, similarity_score


# Sistemin başarısının ölçülmesi için Mean Squared Error'un hesaplandığı fonksiyon.
def scoreCalculator(similarities, scores, score):
    tmp = 0
    predict = []
    for i in range(0, 7):
        x = float(similarities[i].replace("%", "")) / 100 # Similarity score değeri x değişkenine atılır
        predict.append(score * x) # x değişkeni ile kullanıcının girdiği şarkıya verdiği puan çarpılarak tahmin edilen şarkıya verilecek puan tahmin edilir.

    # MSE fonksiyonu uygulanır.
    for i in range(0, 7):
        tmp = tmp + pow(scores[i] - predict[i], 2)
    meanSquareError = tmp / 7

    return Decimal(meanSquareError)  # Değer döndürülmeden önce decimal'e çevrilerek çok küçük değerlerin 'e' sayısıyla ifade edilmesinin önüne geçilmiştir.


# Kullanıcının girdiği şarkının bilgilerinin ekrana yazılmasını sağlayan fonksiyon.
def SongInfo(text):
    album = data_set[data_set['Name'] == text]['Album']
    artist = data_set[data_set['Name'] == text]['Artist']
    song = data_set[data_set['Name'] == text]['Name']
    return "".join(song.values), "".join(artist.values), "".join(album.values)


# Şarkının dataset'te mevcut olup olmadığını belirten fonksiyon.
def isThereinDataSet(text):
    if text in data_set['Name'].values:
        return 1
    return 0
