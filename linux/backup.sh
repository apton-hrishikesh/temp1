#!/bin/bash
FILE = bash_backup_$(date +%Y%m%d).tar.gz
tar -czf $FILE ../bash
echo $FILE
