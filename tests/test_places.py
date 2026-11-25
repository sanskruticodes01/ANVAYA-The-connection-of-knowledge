def test_create_place(client):
    response = client.post("/places", json={"name": "Paris"})
    assert response.status_code == 200
    assert response.json()["name"] == "Paris"

def test_list_places(client):
    client.post("/places", json={"name": "Paris"})
    response = client.get("/places")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_update_place(client):
    client.post("/places", json={"name": "Paris"})
    response = client.put("/places/1", json={"name": "Paris, France"})
    assert response.status_code == 200
    assert response.json()["name"] == "Paris, France"

def test_delete_place(client):
    client.post("/places", json={"name": "Paris"})
    response = client.delete("/places/1")
    assert response.status_code == 200
    response = client.get("/places")
    assert len(response.json()) == 0
