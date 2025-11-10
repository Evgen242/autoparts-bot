#!/bin/bash
THRESHOLD=90
USAGE=$(df / --output=pcent | tail -1 | tr -d ' %')

echo "💾 Disk usage: $USAGE%"

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "🚨 CRITICAL: Disk usage above $THRESHOLD%"
    echo "🔄 Running cleanup..."
    
    # Экстренная очистка
    docker system prune -a -f
    sudo apt clean
    sudo journalctl --vacuum-time=1h
    
    NEW_USAGE=$(df / --output=pcent | tail -1 | tr -d ' %')
    echo "✅ Cleanup completed. New usage: $NEW_USAGE%"
    
    if [ "$NEW_USAGE" -gt "$THRESHOLD" ]; then
        echo "❌ Still critical. Manual intervention required."
        exit 1
    fi
else
    echo "✅ Disk usage is normal"
fi
