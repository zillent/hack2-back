sudo docker run -p 8822:8822 -e "DATABASE_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')" -v $(pwd)/media:/hack2_api/media -d hack2_api
