#!/bin/bash
PORT=8080
if [ -n ${1} ]; then
    PORT=${1}
fi
echo "my life is $PORT"
npm start
