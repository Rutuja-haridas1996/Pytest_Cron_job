#!/bin/sh
DIR=`date +%m%d%y`
DEST=./backup/$DIR
mkdir $DEST
echo $DEST
mongodump --db mooveit_db --gzip -o $DEST