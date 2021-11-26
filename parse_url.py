from urllib import parse
def parse_query(query:str) -> dict:
    return dict(
        parse.parse_qsl(
            parse.urlsplit(query).query
        )
    )

if __name__ == '__main__':

    assert parse_query('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_query('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse_query('https://example.com/') == {}
    assert parse_query('https://example.com/?') == {}
    assert parse_query('https://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse_query('https://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse_query('https://google.com/search?query=JavaScript') == {'query': 'JavaScript'}
    assert parse_query('http://site.com:8080/path/page?p1=v1&p2=v2') == {'p1': 'v1','p2':'v2'}
    assert parse_query('http://examples.net/') == {}
    assert parse_query('https://example.com/path/to/page?name=ferret&color=purple&age=2') == {'name': 'ferret', 'color': 'purple','age':'2'}

