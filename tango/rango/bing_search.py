# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

BING_API_KEY = "kcTmVU4cCy07Krfzy7MAxZodIgChneDI9jBRFg7VOEU"


def run_query(search_terms):
    root_url = "https://api.datamarket.azure.com/Bing/Search/v1/"
    source = "Web"

    results_per_page = 10
    offset = 0
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)
    username = ''

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)

    results = []

    try:
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        response = urllib2.urlopen(search_url).read()

        json_response = json.loads(response)

        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'].encode('utf-8'),
                'link': result['Url'].encode('utf-8'),
                'summary': result['Description'].encode('utf-8')})
    except urllib2.URLError, e:
                print "Error when querying the Bing API: ", e
    return results


def main():
    a = run_query("football")
    for i in a:
        print i['title']


if __name__ == "__main__":
    main()
