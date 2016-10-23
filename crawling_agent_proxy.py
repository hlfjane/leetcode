import urllib2
import re
import itertools

max_errors = 5

num_errors = 0

#url = 'www.putclub.com'

def download(url, num_retry = 2):
    print 'downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'download error:', e.reason
        if num_retry > 0:
            hasattr(e, 'code') and 500 <= e.code < 600
            print 'num_retry = ', num_retry
            num_retry = num_retry - 1
            return download(url, num_retry - 1)
        else:
            html = None
    return html

def download_by_id(file_download):
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/Afghanistan-%d' %page
        html = download(url)
        file_download.write(html)
        if html is None:
            num_errors += 1
            break
        else:
            num_errors = 0 

def download_by_link(seed_url, link_regex):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link)
                crawl_queue.append(link)


def get_link(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

def main():
    f=open('download.txt','wa')

    download_by_id(f)
    f.close()
#content = download('https://www.google.com.hk')
    print num_errors

main()
