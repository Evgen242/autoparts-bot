#!/bin/bash
echo "💾 Storage Manager - $(date)"

# Проверяем использование диска
echo "📊 Disk usage:"
df -h /

# Проверяем Docker использование
echo "🐳 Docker disk usage:"
docker system df

# Анализируем большие директории
echo "📁 Large directories:"
sudo du -sh /home/* 2>/dev/null | sort -hr | head -10
sudo du -sh /var/lib/docker/* 2>/dev/null | sort -hr | head -10

# Рекомендации
USAGE=$(df / --output=pcent | tail -1 | tr -d ' %')
if [ "$USAGE" -gt 90 ]; then
    echo "🚨 RECOMMENDATION: Disk usage critical - consider upgrading to larger disk"
elif [ "$USAGE" -gt 80 ]; then
    echo "⚠️  RECOMMENDATION: Disk usage high - monitor closely"
else
    echo "✅ RECOMMENDATION: Disk usage normal"
fi
