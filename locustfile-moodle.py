from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})

    @task
    def hello_world(self):
        self.client.get("/admin")
        self.client.get("/analytics")
        self.client.get("/auth")
        self.client.get("/backup")
        self.client.get("/cache")
        self.client.get("/local")
        self.client.get("/report")
        self.client.get("/user")
        self.client.get("/privacy")

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")