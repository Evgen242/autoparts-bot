#!/bin/bash
DBS=$(sudo -u postgres psql -t -c "SELECT datname FROM pg_database WHERE datistemplate = false;" | xargs)

for db in $DBS; do
  echo "🔍 Проверка базы: $db"
  sudo -u postgres psql -d "$db" -c "SELECT COUNT(*) FROM autoparts;" 2>/dev/null
  sudo -u postgres psql -d "$db" -c "SELECT COUNT(*) FROM parts;" 2>/dev/null
done
