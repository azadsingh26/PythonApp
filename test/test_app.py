from src.app import app

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200

def test_other_path():
    tester = app.test_client()
    response = tester.get("/*", content_type="html/text")

    assert response.status_code == 404
