import os
from pydo import Client

client = Client(token=os.environ.get("DIGITALOCEAN_TOKEN"))

create_resp = client.apps.create(
    {
        "spec": {
            "name": "web-app",
            "region": "nyc",
            "services": [
                {
                    "name": "api",
                    "github": {},
                    "run_command": "bin/api",
                    "environment_slug": "node-js",
                    "instance_count": 2,
                    "instance_size_slug": "basic-xxs",
                    "routes": [],
                }
            ],
        }
    }
)
