# Returns 5 lists, each containing 1 dictionary of information about movies.

import glob
import os
import sys
import requests

MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'
files = glob.glob(os.path.join(TMP, '*json'))

BASE_URL = (f'http://projects.bobbelderbos.com/pcc/omdb/')

def get_movie_data(files=files):
    """return a list of movie dicts"""
    for json_url_slug in files:
        clean_slug = (json_url_slug.split('/')[2])
        json_urls = (f'http://projects.bobbelderbos.com/pcc/omdb/{clean_slug}')
        with requests.Session() as session:  # will close the session when done with it
            listofmovies = []
            try:
                response = session.get(json_urls)
                dict_object = (dict(response.json()))
                listofmovies.append(dict_object)
            except BaseException as error:
                print("get", type(error), error, file=sys.stderr)
                sys.exit(1)
        return listofmovies


get_movie_data()
