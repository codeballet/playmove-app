from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        # home page should respond with success 200
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        # terms page should respond with success 200
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        # privacy page should respond with success 200
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200
