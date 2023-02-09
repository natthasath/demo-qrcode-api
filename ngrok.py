from pyngrok import ngrok

http_tunnel = ngrok.connect(8000, "http")
tunnels = ngrok.get_tunnels()
ngrok_process = ngrok.get_ngrok_process()
print(tunnels)

try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down server.")
    ngrok.kill()