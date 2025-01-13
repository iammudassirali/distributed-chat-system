#!/bin/bash
# Initialize MongoDB Replica Set
echo "Setting up MongoDB Replica Set..."

# MongoDB Replica Set initiation
mongo --eval "rs.initiate()"

# Create an index on 'timestamp' for better query performance
mongo --eval "db.getCollection('messages').createIndex({timestamp: 1})"
