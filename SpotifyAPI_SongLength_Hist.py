
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# クライアントIDとクライアントシークレットIDの入力
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="【client_ID】",
                                                           client_secret="【client_secret_ID】"))

# アーティストのIDを取得
artist_name = "【好きなアーティスト名】"
results = sp.search(q=artist_name, type="artist")
artist_id = results["artists"]["items"][0]["id"]

# APIリクエストを送信して曲の一覧を取得
results = sp.search(q=artist_name, type="track", limit=50)
tracks = results["tracks"]["items"]

# 取得した曲数の表示
print("Number of tracks found: ", len(tracks))

# 各曲の時間を取得して表示
durations = []
for track in tracks:
    features = sp.audio_features(track["id"])
    duration = features[0]["duration_ms"] / 1000
    durations.append(duration)
    print("「{0}」, {1:.2f}s".format(track["name"], duration))

# 取得した時間をヒストグラムに表示
plt.hist(durations, bins=20)
plt.xlabel("Song length (s)")
plt.ylabel("frequency")
plt.title("Histgram of Song length")
plt.show()
