# class Itunes:
#
#     def __init__(self):
#         pass
#
#     def songlookup(self):
#         artist = input("Give a music artist's name.")
#         import requests
#         myurl = "https://itunes.apple.com/search?term="
#         artist = artist.strip(" ")
#         artist.replace(" ", "+")
#         newartist = artist.lower()
#         try:
#             fullurl = myurl + newartist
#             r = requests.get(fullurl)
#             data = r.json()
#             songlist = []
#             i = 0
#
#             def devlist(i):
#                 while len(songlist) < 5:
#                     songlist.append(data["results"][i]["trackName"])
#                     i += 1
#                 repeat = []
#                 for songs in songlist:
#                     if songs not in repeat:
#                         repeat.append(songs)
#                         continue
#                     else:
#                         songlist.remove(songs)
#
#             devlist(i)
#             i = len(songlist) + 1
#             if len(songlist) < 5:
#                 devlist(i)
#             songlist1 = songlist[0:len(songlist) - 1]
#             songlist2 = songlist[-1]
#             newstring = ""
#             for songs in songlist1:
#                 newstring = newstring + songs + ", "
#             print(" ")
#             return artist + "'s top five songs are " + newstring + "and " + songlist2 + "."
#         except:
#             return "Oops! There was an error."
#
#
# if __name__ == '__main__':
#
#     song = Itunes()
#     print("Welcome to the song lookup!")
#     print(song.songlookup())
#https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
class Itunes:

    def songlookup():
        artist = input("Give a music artist's name.")
        import requests
        myurl = "https://itunes.apple.com/search?term="
        artist = artist.strip(" ")
        artist.replace(" ", "+")
        newartist = artist.lower()
        try:
            fullurl = myurl + newartist
            r = requests.get(fullurl)
            data = r.json()
            # print(data)
            songlist = []
            i = 0
            artwork = ""

            def devlist(i):
                while len(songlist) < 5:
                    songlist.append(data["results"][i]["trackName"])
                    print(data["results"][i]["artworkUrl60"])
                    i += 1
                repeat = []
                for songs in songlist:
                    if songs not in repeat:
                        repeat.append(songs)
                        continue
                    else:
                        songlist.remove(songs)

            devlist(i)
            i = len(songlist) + 1
            if len(songlist) < 5:
                devlist(i)
            songlist1 = songlist[0:len(songlist) - 1]
            songlist2 = songlist[-1]
            newstring = ""
            for songs in songlist1:
                newstring = newstring + songs + ", "
            print(" ")
            print(artist + "'s top five songs are " + newstring + "and " + songlist2 + ".")
            action = input("Would you like to see another? [Y] or [N]?").upper()
            if action == 'Y':
                Itunes.songlookup()
            else:
                print("Okay, bye!")
        except:
            return "Oops! There was an error."


if __name__ == '__main__':

    print("Welcome to the song lookup!")
    Itunes.songlookup()