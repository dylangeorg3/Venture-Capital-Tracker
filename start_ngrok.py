from pyngrok import ngrok

# Start an ngrok tunnel to localhost:8000
public_url = ngrok.connect(8000)
print("Ngrok tunnel open at:", public_url)
input("Press Enter to close the tunnel...")
ngrok.disconnect(public_url)