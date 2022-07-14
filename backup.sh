#!/bin/bash
FILE=script_backup_$(date +%Y%m%d).tar.gz
tar -czf $FILE linux
echo $FILE
