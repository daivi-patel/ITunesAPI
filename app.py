from flask import render_template, Flask, request
import requests

app = Flask(__name__)



@app.route("/")
def base():
    """
    routes to base url/page
    :return: base.html
    """
    return render_template("base.html")

@app.route("/cont")
def cont():
    """
    routes to lookup page
    :return: lookup.html
    """
    return render_template("lookup.html")

@app.route('/output', methods=['POST', 'GET'])
def output():
    """
    routes to a display page or
    routes to a login error function
    :return: display.html
    """
    output = request.form
    artist = request.form.get('Artist')
    myurl = "https://itunes.apple.com/search?term="
    artist = artist.strip(" ")
    artist.replace(" ", "+")
    newartist = artist.lower()
    try:
        fullurl = myurl + newartist
        r = requests.get(fullurl)
        data = r.json()
        songlist = []
        i = 0

        def devlist(i):
            while len(songlist) < 5:
                songlist.append(data["results"][i]["trackName"])
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
        artwork = data["results"][0]["artworkUrl60"]
        # print(" ")
        # print(artist + "'s top five songs are " + newstring + "and " + songlist2 + ".")
    except:
        return "Oops! There was an error."
    return render_template("display.html", artist = artist, newstring = newstring,
                           songlist2 = songlist2, artwork = artwork)

if __name__ == '__main__':
    app.run(debug=True)