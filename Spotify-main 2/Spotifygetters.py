# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:26:17 2022

@author: Jonathan
"""

#Rate limiting kommer vara ett problem.- Den "buffrar requests
#Hur kommer vi att använda en token sen?
#hur gittar vi stats för antalet streamningar

import requests

Token= 'BQDDr6Gv01gnNgMaMuLJrN0pu9uLUvrdaeF-L87_Qy_AgOS0LX6MYVLA6L5Hm1QKg5tXF_GDtEqCCNdnJT8QO3oypCx0W-aPOFeme3hxkl84mw6SSLPk8AeQrnYQOYK7TmDTFMed5HWeZ7jB'
album="5Z9iiGl2FcIfa3BMiv6OIw"
song_ID="4cOdK2wGLETKBW3PvgPWqT"
artist_ID="0gxyHStUsqpMadRV0Di1Qt"   # start ID

def get_album_info(album,Token):
    album_info = requests.get("https://api.spotify.com/v1/albums/"+album,
                              headers={
                                  "Authorization" :f"Bearer {Token}"
                                  }
                              )
    return album_info.json()


def get_song_info(song_ID,Token):
    song_info= requests.get("https://api.spotify.com/v1/tracks/"+song_ID,
                              headers={
                                  "Authorization" :f"Bearer {Token}"
                                  }
                              )
    return song_info.json()


def get_audio_features(song_ID,Token):
   song_features= requests.get("https://api.spotify.com/v1/audio-features/"+song_ID,
                              headers={
                                  "Authorization" :f"Bearer {Token}",
                                  }
                             )
   return song_features.json()


def get_artist_info(artist_id,Token):
   artist_info = requests.get("https://api.spotify.com/v1/artists/"+artist_id,
                              headers={
                                  "Authorization" :f"Bearer {Token}"
                                  }
                             )
   return artist_info.json()

    
def get_related_artists(artist_ID,Token):
   related_artists = requests.get("https://api.spotify.com/v1/artists/"+artist_ID+"/related-artists",
                            headers={
                                 "Authorization" :f"Bearer {Token}"
                                  }
                             )
   return related_artists.json()


def get_artist_albums(artist_ID,Token): 
    offset=0
    artist_albums = requests.get("https://api.spotify.com/v1/artists/"+artist_ID+"/albums?limit=10",
                            headers={
                                 "Authorization" :f"Bearer {Token}"
                                  }
                             ).json()
    while artist_albums["limit"]< artist_albums["total"]:
        offset+=50
        artist_albums_new = requests.get("https://api.spotify.com/v1/artists/"+artist_ID+"/albums?limit=50&offset="+str(offset),
                             headers={
                                 "Authorization" :f"Bearer {Token}"
                                  }
                                 ).json()
        artist_albums["items"] = artist_albums["items"]+artist_albums_new["items"]
        artist_albums["limit"] = artist_albums["limit"]+artist_albums_new["limit"]

    return artist_albums


# #%%
# import threading


# def do_request():
#     requests=0
#     x=scan_album(album,Token)
#     while True:
#         try:
#             while(x["type"]=="album"):
#                 x=scan_album(album,Token)
#                 requests+=1
#                 print(requests)
#         except:
#             print("Failed")
    
# threads = []

# for i in range(1):
#     t=threading.Thread(target=do_request)
#     t.daemon=True
#     threads.append(t)

# for i in range(1):
#     threads[i].start()
    
# for i in range(1):
#     threads[i].join()
    
    
    # album=scan_album(album)
# song=scan_song(song_ID)
# song_features=Audio_features(song_ID)
# artist_info=get_artist_info(artist_ID)
# related_artists=get_related_artists(artist_ID)


# new_artists_ID=[]
# for i in range(len(related_artists["artists"])):
#     new_artists_ID.append(related_artists["artists"][i]["uri"].split(":")[2])


# artist_albums={}
# for artist_ID in new_artists_ID:
#     artist_albums[artist_ID]=(get_artist_albums(artist_ID)["items"],get_artist_info(artist_ID))

# pd.DataFrame(artist_albums).to_excel("test1.xlsx")




    
    
    
