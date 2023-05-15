import csv
from locust import HttpUser, task, between
from random import choice

class UserBehavior(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        self.token = None
        self.user = self.load_user()
        self.login()

    def load_user(self):
        with open('users.csv', 'r') as f:
            reader = csv.DictReader(f)
            return choice(list(reader))

    def login(self):
        response = self.client.post("/auth/login", json={
            "username": self.user['username'],
            "password": self.user['password']
        })
        self.token = response.json()['token']
        self.client.headers.update({'Authorization': f'Bearer {self.token}'})

    @task(2)
    def get_profile(self):
        self.client.get("/user/profile")

    @task(1)
    def update_profile(self):
        self.client.put("/user/profile", json={
            "email": self.user['email'],
            "name": self.user['name']
        })

    @task(3)
    def list_todos(self):
        self.client.get("/todos")

    @task(2)
    def create_todo(self):
        self.client.post("/todos", json={
            "title": "New todo",
            "completed": False
        })

    @task(2)
    def get_todo(self):
        # Assume todo IDs range from 1 to 100
        todo_id = choice(range(1, 101))
        self.client.get(f"/todos/{todo_id}")

    @task(1)
    def update_todo(self):
        # Assume todo IDs range from 1 to 100
        todo_id = choice(range(1, 101))
        self.client.put(f"/todos/{todo_id}", json={
            "title": "Updated todo",
            "completed": True
        })

    @task(1)
    def delete_todo(self):
        # Assume todo IDs range from 1 to 100
        todo_id = choice(range(1, 101))
        self.client.delete(f"/todos/{todo_id}")

# To run:
# locust -f locust_script.py --host=http://localhost:4010
            