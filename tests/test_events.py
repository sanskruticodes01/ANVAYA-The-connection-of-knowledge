def test_create_event(client):
    response = client.post(
        "/events",
        json={"title": "Storming of the Bastille", "year": 1789},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Storming of the Bastille"
    assert response.json()["year"] == 1789