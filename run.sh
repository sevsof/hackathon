#!/bin/bash
# https://habr.com/ru/articles/47163/
if [ -d 'inbox' ]; then
    python3 src/main.py
else
    echo "Данного файла нет, ошибка"
fi