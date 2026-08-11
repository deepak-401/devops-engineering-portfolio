from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
def test_app_name():
    client = app.test_client()
    response = client.get("health")
    assert response.status_code == 200
    assert response.json["application"] == "CloudXDeepak DevOps Demo"
