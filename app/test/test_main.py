def test_blooskyn_tattoo(client):
    response = client.get("/")
    assert b"Blooskyn Tattoo" in response.data