from app import create_app

app = create_app()
with app.test_client() as c:
    resp = c.get('/posts')
    print('/posts', resp.status_code)
    try:
        print(resp.data.decode('utf-8'))
    except Exception as e:
        print('Error reading /posts response:', e)
    resp2 = c.get('/post')
    print('/post', resp2.status_code)
    try:
        print(resp2.data.decode('utf-8'))
    except Exception as e:
        print('Error reading /post response:', e)
