import itertools

max_errors = 5

num_errors = 0

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' %page
    html = download()
