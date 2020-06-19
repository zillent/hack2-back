sudo docker run -p 8811:8811 -e "DATABASE_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')" -v $(pwd)/media:/hack2/media -d hack2_api
