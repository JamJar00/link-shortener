ROUTES = {
  "goog": "httpsm://google.co.uk"
}

def main(args):
  name = args["http"]["path"]

  print(f"Received request for '{name}'");
  redirect_url = ROUTES.get(name, "https://jread.dev")

  return {
    "statusCode": 302,
    "headers": {
      "Location": redirect_url
    }
  }
