from urllib.parse import urlparse

def url_parser(url):
    parts = urlparse(url)
    directories = parts.path.strip('/').split('/')
    queries = parts.query.strip('&').split('&')

    elements = {
        'scheme': parts.scheme,
        'netloc': parts.netloc,
        'path': parts.path,
        'params': parts.params,
        'query': parts.query,
        'fragment': parts.fragment,
        'directories': directories,
        'queries': dict(map(lambda x: x.split('='), queries)),
    }

    return elements

print(url_parser("https://example.com/path/to/page?name=ferret&color=purple"))
print(url_parser("https://example.com/?name=Dima"))
print(url_parser("https://example.com/path/to/page?name=ferret&color=purple&"))
print(url_parser("https://www.youtube.com/watch?v=xRv9Uq1ffbg&list=PLxbd7ySXT5YoTo79ZN4Lo75WADbTDMK4v&index=64&ab_channel=%D0%9C%D0%B8%D1%85%D0%B0%D0%B8%D0%BB%D0%A0%D1%83%D1%81%D0%B0%D0%BA%D0%BE%D0%B2"))
print(url_parser("https://lms.ithillel.ua/groups/612355f386b02c38d884ecf4/homeworks/61995aa4e1fae77747ae897f"))






