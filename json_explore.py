__author__ = 'rsukla'


# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}

def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt   # this is basically a dictionary {'query': 'artist:Lucero', 'fmt': 'json'}
    r = requests.get(url + uid, params=params)  # <Response [200]>
    print "requesting", r.url
    print r.json()
    if r.status_code == requests.codes.ok:
        return r.json()   # getting the json  dictionary here
    else:
        r.raise_for_status()

def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AND KIT")  #We are going to use the search query first so that we can use ID
    pretty_print(results)   #The response we get is JSON data

    artist_id = results["artists"][1]["id"]  # jo artist kya id aaya hain usse se sab information pata lag jayegi
    print "\nARTIST:"
    pretty_print(results["artists"][1])  # second object we are highlAy interested here

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)  # mujhe artist ka id mil gaya
    releases = artist_data["releases"]
    print "\nONE RELEASE:"   # phele dictionary then list then dictionary ...so try to move accordingly
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]
                                                                    #JSON object is Python dictionary
    print "\nALL TITLES:"
    for t in release_titles:  # go through the titles
        print t

if __name__ == '__main__':
    main()

'''
three different get function request we can perform here

On each entity resource, you can perform three different GET requests:

 lookup:   /<ENTITY>/<MBID>?inc=<INC>
 browse:   /<ENTITY>?<ENTITY>=<MBID>&limit=<LIMIT>&offset=<OFFSET>&inc=<INC>
 search:   /<ENTITY>?query=<QUERY>&limit=<LIMIT>&offset=<OFFSET>

'''