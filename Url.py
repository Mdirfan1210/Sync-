import pyshorteners
url=input('Enter the url: ')
def shortenerurl(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))
shortenerurl(url)