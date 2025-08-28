## Grafana Loki
it is a log aggregation tool which help us to reduce cost by only logging metadata like labels and it makes it lightwegith and affordable.
it can also intergate with grafana which is a popular visulization tool.

### Docker setup 
- run `docker run -d -p 3100:3100 grafana/loki:3.0.0`
- it will run on `http://localhost:3100`
- to check it is running go to `http://loclahost:3100/ready` if it says ready it is running.

## Grafana Alloy
it is the tool which will help us to send the application log to the grafana loki.

