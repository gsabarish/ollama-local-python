    import requests

    OLLAMA_BASE_URL = "http://localhost:11434"

    def test_connection():
        try:
            response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Connection failed: {e}")
            return False

    def generate_text(prompt, model="llama3.2"):
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
        return response.json()["response"]

    if __name__ == "__main__":
        if test_connection():
            print("Connected to Ollama!")
            response = generate_text("Explain what a neural network is in 2 sentences.")
            print(response)
        else:
            print("Could not connect to Ollama. Is it running?")