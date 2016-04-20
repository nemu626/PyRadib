import codecs
import urllib2
import sys
import BeautifulSoup
import re

BASEURL = "http://radibrary.tistory.com"
tempurl = "http://radibrary.tistory.com/27928"
TAGURL = "http://radibrary.tistory.com/tag/"
def tagpage(tag):
    return TAGURL + tag

def _parse_pages_from_tagpage(listurl):
    linklist = []
    html = urllib2.urlopen(listurl).read().decode('utf-8','ignore')
    soup = BeautifulSoup.BeautifulSoup(html)

    pages = soup.find('div',{"class":"paging"})
    print pages

    alist = soup.findAll("a")

    pattern = r"\[\d{4}\.\d{2}\.\d{2}\](.*)#\d+.*"
    cmpl = re.compile(pattern)

    linklist = [[l.text,l.get('href')] for l in alist if re.match(pattern,l.text)]
    for l in linklist:
        l[1] = BASEURL + l[1]
    return linklist


def parseALinks(urlstring):
    html = urllib2.urlopen(urlstring).read().decode('utf-8','ignore')
    soup = BeautifulSoup.BeautifulSoup(html)
    alist = soup.findAll("a")

    linklist = []

    t = [[l.text,l.get("href")] for l in alist if l.text.endswith("7z")]
    linklist.extend(t)

    for i in range(1,999):
        add = [[l.text,l.get("href")] for l in alist if l.text.endswith("7z." + '{0:03d}'.format(i))]
        if add :
            linklist.extend(add)
        else :
            break

    return linklist

def downloadAllList(linklist):
    for link in linklist:
        file = urllib2.urlopen(link[1])
        with open(link[0],'wb') as f:
            print "Downloading   : " + link[0] + ", Please Wait..."
            f.write(file.read())
        print "DownLoad file : " + link[0] + ", Complete."
    print "Download finished."


if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[1] == "-tag":
            _parse_pages_from_tagpage(tagpage(sys.argv[2]))
        elif sys.argv[1] == "-one":
            downloadAllList(parseALinks(sys.argv[2]))
