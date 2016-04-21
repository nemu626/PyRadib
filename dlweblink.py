import codecs
import urllib2
import sys
import BeautifulSoup
import re

BASEURL = "http://radibrary.tistory.com"
tempurl = "http://radibrary.tistory.com/27928"
TAGURL = "http://radibrary.tistory.com/tag/"
PAGEQ = "?page="

def tagpage(tag):
    return TAGURL + tag

def parse_pages_from_tagpage(tagpage):
    postlist = []
    html = urllib2.urlopen(tagpage).read().decode('utf-8','ignore')
    soup = BeautifulSoup.BeautifulSoup(html)

    pages = soup.find('div',{"class":"paging"})
    r = pages.findAll('a')
    r.pop()
    # this is a Last Page...
    last_pagenum = int(r.pop().text.strip("#"))
    
    
    
    for i in range(1,last_pagenum+1):
        pageurl = tagpage + PAGEQ + str(i)
        html = urllib2.urlopen(pageurl).read().decode('utf-8','ignore')
        soup = BeautifulSoup.BeautifulSoup(html)

        alist = soup.findAll("a")
        pattern = r"\[\d{4}\.\d{2}\.\d{2}\](.*)#\d+.*"
        cmpl = re.compile(pattern)

        postlist.extend([[l.text,l.get('href')] for l in alist if re.match(pattern,l.text)])
    postlist = map(lambda x: [x[0],BASEURL + x[1]],postlist)
    return postlist
    


def parse_links(posturl):
    html = urllib2.urlopen(posturl).read().decode('utf-8','ignore')
    soup = BeautifulSoup.BeautifulSoup(html)
    alist = soup.findAll("a")

    filelist = []

    t = [[l.text,l.get("href")] for l in alist if l.text.endswith("7z")]
    filelist.extend(t)

    for i in range(1,999):
        add = [[l.text,l.get("href")] for l in alist if l.text.endswith("7z." + '{0:03d}'.format(i))]
        if add :
            filelist.extend(add)
        else :
            break
    return filelist

# filelist : list of [filename,fileurl]
# return None
def download_files(filelist):
    for link in filelist:
        file = urllib2.urlopen(link[1])
        with open(link[0],'wb') as f:
            print "Downloading   : " + link[0] + ", Please Wait..."
            f.write(file.read())
        print "DownLoad file : " + link[0] + ", Complete."
    print "Download finished."
    
def confirm_tagpages_download(postlist):
    print "=========== DOWNLOAD LIST  ============"
    for p in postlist:
        print p[0]
    
    print "Will You Download listed ALL files?(y,n)"
    result = input()
    if result == "y" or result == "Y":
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[1] == "-tag":
            a = parse_pages_from_tagpage(tagpage(sys.argv[2]))
            confirm_tagpages_download(a)
        elif sys.argv[1] == "-one":
            download_files(parse_links(sys.argv[2]))


