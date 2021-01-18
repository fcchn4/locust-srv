from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/wp-admin", json={"username":"foo", "password":"bar"})

    @task
    def hello_world(self):
        self.client.get("/wp-admin")
        self.client.get("/wp-content")
        self.client.get("/wp-content")

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")