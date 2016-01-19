#!/usr/bin/env bash

gcc helloworld.c -o hello
python -m unittest discover
