def test_create_place(client):
    response = client.post("/places", json={"name": "Paris"})
    assert response.status_code == 200
    assert response.json()["name"] == "Paris"

def test_list_places(client):
    client.post("/places", json={"name": "Paris"})
    response = client.get("/places")
    assert response.status_code == 200
    assert len(response.json()) == 1