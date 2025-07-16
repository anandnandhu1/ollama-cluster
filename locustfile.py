from locust import HttpUser, task, between

# This class represents a fake user sending requests to Ollama
class OllamaUser(HttpUser):
    # Wait between 1 and 2 seconds between each request
    wait_time = between(1, 2)

    @task
    def send_request_to_ollama(self):
        # This is the input we send to the LLM
        request_data = {
            "model": "gemma:3b",
            "prompt": "What is DevOps? Explain simply.",
        }

        # Send a POST request to the Ollama server
        self.client.post("/api/generate", json=request_data)
