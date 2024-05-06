# Instructions

```bash
# build 
docker build -t report .
# run
docker run -p 5000:5000 report
# test it
curl http://localhost:5000/reports
```