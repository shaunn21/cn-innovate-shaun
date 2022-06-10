
#! 1st activity -

from re import X


c_dict = {
    "uk":"london",
    "france":"paris",
    "germany":"munich",
    "italy":"rome"
}
print(c_dict)

c_dict.setdefault("spain", "madrid")
c_dict.setdefault("usa", "washington")
print (c_dict)

update1 = {"uk":"english", "france":"french", "germany":"german","italy":"italian","spain":"spanish","usa":"american"}
c_dict.update(update1)
print (c_dict)


#! 2nd activity --

fav_songs = [
    {
        'id':1,
        'artist' : 'pendulum',
        'song_name': 'come alive',
        'genre' : 'rock',
        'year' : '2021'
    },
    {
        'id':2,
        'artist' : 'the weekend',
        'song_name': 'blinding lights',
        'genre' : 'pop',
        'year' : '2020'
    },
    {
        'id':3,
        'artist' : 'eminem',
        'song_name': 'rap god',
        'genre' : 'rap',
        'year' : '2020'
    },
    {
        'id':4,
        'artist' : 'metallica',
        'song_name': 'enter sandman',
        'genre' : 'rock',
        'year' : '1984'
    }
]

def printSongs():
    for song in fav_songs:
        print(song)
    
    print("-------------")       

songToAdd = {
    'id': 5,
    'artist': 'Bob Marley',
    'song_name': 'Is This Love',
    'genre': 'reggae',
    'year': '1978'
}

def addToFavSongs(toAdd):
    fav_songs.append(toAdd)

addToFavSongs(songToAdd)

printSongs()

def removeSongFromFavBySongName(toRemove):
    for i in range(len(fav_songs)):
        if fav_songs[i]['song_name'] == toRemove:
            del fav_songs[i]
            break    
    
removeSongFromFavBySongName('rap god')

printSongs()

def updateSongByID(toEdit):
    artist_name = input('Type here: ')
    song_name = input('Type here: ')
    genre_name = input('Type here: ')
    year_name = input('Type here: ')
    for i in range(len(fav_songs)):
        if fav_songs[i]['id'] == toEdit:
            fav_songs[i]['artist'] = artist_name
            fav_songs[i]['song_name'] = song_name
            fav_songs[i]['genre'] = genre_name
            fav_songs[i]['year'] = year_name
            break 

updateSongByID(2)

printSongs()
