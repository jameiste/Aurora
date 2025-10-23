# Leave it up mostly
.DEFAULT_GOAL := up

# Build and start container
up:
	docker compose up -d --build

# View logs live
logs:
	docker logs -f aurora-alert

# Stop container
down:
	docker compose down

# Rebuild 
rebuild:
	docker compose build --no-cache

# Show running containers
ps:
	docker compose ps

# Clean everything up
clean:
	docker compose down -v
	docker system prune -f
