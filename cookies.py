from http.cookies import SimpleCookie

def parse_cookie(query:str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {}
    for key,morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies





if __name__ == '__main__':

    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('color=Black;car=audi;') == {'color': 'Black', 'car': 'audi'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Max=User;password=112233;') == {'name': 'Max=User', 'password': '112233'}
    assert parse_cookie('name=Dima=User;age=28;height=180') == {'name': 'Dima=User', 'age': '28','height': '180'}
    assert parse_cookie('size=XL;color=red') == {'size':'XL','color':'red'}