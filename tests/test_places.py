def test_create_place(client):
    response = client.post("/places", json={"name": "Paris"})
    assert response.status_code == 200
    assert response.json()["name"] == "Paris"