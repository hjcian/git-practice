#!/bin/sh
COMMIT_MSG_FILE="$1"
echo "[commit-msg] commit file is in $COMMIT_MSG_FILE"
MSG=`cat ${COMMIT_MSG_FILE}`
echo "[commit-msg] Commit msg is ${MSG}"