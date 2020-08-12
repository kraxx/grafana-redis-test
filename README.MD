# Grafana with Redis Plugin

## Intro

TODO: < PROBLEM TO SOLVE >
- memcached has no grafana plugin at this moment
- redis does, with the official redistimeseries by redislabs
- does not require an external database
- can only display meterics on database values
- metadata and resources must be exported using an exporter to another datastore

## Redis

- Simple key-value storage
- redistimeseries, a redis with additional support for adding time as a metric
- uses (probably fact check) a JSON object store internally

## Grafana

- Grafana is a timeseries data visualization tool
- Reads from timeseries databases and creates pretty graphs
- Has official plugins as well as custom community plugins
- So, install the redis plugin
- Use custom Dockerfile so we don't need to keep installing the plugin

## Script

- Simple python script to create two metrics for fruits we're interested in: price and stock
- Sets baseline values to 50 for both metrics
- Every second, randomly decrements/increments a price and stock by a small amount, for a fruit selected at random

## Docker

- Containerize it all so we don't worry about dependencies.
- Run it all in docker-compose so we don't worry about complicated deploys

## Running it + Pretty graphs

Yep that's right

## Closing statement

- Redis works well, it's simple, it's clean, you can see things real time in Grafana
- If you want metadata like GETS/SETS/etc. and memory usage, must use exporter.