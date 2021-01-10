# Website Uptime Monitor

This is a python application that can be used to monitor the status of multiple websites.

## Installation

Clone the repository :)

## Usage

Use the base configuration template `config.example.json` to configure the application. 

Required parameters:
- url: website/endpoint to be monitored
- method: only supports get/post for the time being (note: post doesn't currently support passing data)
- expectStatus: the expected http status code
- maxLatency: the latency in MS not to exceed

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
