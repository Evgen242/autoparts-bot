#!/bin/bash
echo "🧹 Cleaning up Docker resources..."

# Удаляем остановленные контейнеры
docker container prune -f

# Удаляем неиспользуемые образы
docker image prune -a -f

# Удаляем неиспользуемые тома
docker volume prune -f

# Удаляем неиспользуемые сети
docker network prune -f

echo "✅ Cleanup completed"
