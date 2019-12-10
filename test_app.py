import unittest
from app import calculate_amount, app, url_for
import json
import os


class TestClass(unittest.TestCase):
    def setUp(self):
        # self.app = app.test_client()
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_calculate_amount(self):
        self.assertEqual(10 == calculate_amount(get_json_from_file("test_data/rented_book_items.json")), True)

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_statement(self):
        response = self.client.get("/statement")
        self.assertEqual(response.status_code, 200)

    def test_calculate(self):
        payload = get_json_from_file("test_data/rented_book_items.json")
        amount = calculate_amount(payload)
        response = self.client.post("/calculate", data=json.dumps(payload), headers={"Content-Type": "application/json"})
        response = json.loads(response.data.decode().replace("'", '"'))
        self.assertEqual(response, { "url": "/statement?amount=" + str(amount)})

    def test_calculate_fail(self):
        payload = get_json_from_file("test_data/fail_rented_book_items.json")
        response = self.client.post("/calculate", data=json.dumps(payload),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)

def get_json_from_file(filename):
    file_content = read_local_file(filename)
    response = json.loads(file_content)
    return response

def read_local_file(relative_path_filename):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, relative_path_filename)
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    unittest.main()