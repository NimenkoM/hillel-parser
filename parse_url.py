from urllib import parse

def url_parser(qeary:str) -> dict:
    url = "http://www.example.org/default.html?ct=32&op=92&item=98"
    url = url.split("?")[1]
    dict = {x[0]: x[1] for x in [x.split("=") for x in url[1:].split("&")]}



if __name__ == '__main__':

    # Testing function `parse`
    assert url_parser('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert url_parser('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert url_parser('https://example.com/') == {}
    assert url_parser('https://example.com/?') == {}
    assert url_parser('https://example.com/?name=Dima') == {'name': 'Dima'}





