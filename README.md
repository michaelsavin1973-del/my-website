# Docker Flask Nginx Demo

Simple DevOps project demonstrating:

- Docker Compose
- Nginx Reverse Proxy
- Python Flask API
- Frontend HTML page

## Architecture

Browser
-> Nginx
-> Flask API

## Services

### Web

Nginx frontend available on:

http://localhost:8080

### Backend

Flask API endpoint:

http://localhost:8080/api

## Run

```bash
docker compose up -d
