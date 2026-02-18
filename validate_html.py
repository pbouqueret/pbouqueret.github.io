
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass

parser = MyHTMLParser()
try:
    with open('index.html', 'r') as f:
        parser.feed(f.read())
    print("HTML parsed successfully")
except Exception as e:
    print(f"Error parsing HTML: {e}")
