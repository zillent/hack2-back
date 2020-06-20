sudo docker run -p 8823:8823 -e "DATABASE_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')" -v $(pwd)/media:/hack2_user_api/media -d hack2_user_api
