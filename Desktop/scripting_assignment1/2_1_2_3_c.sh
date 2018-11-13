#!/bin/bash
ifconfig|sed -n -E '/(([0-9]|[a-f]){2}[:-]){5}([0-9]|[a-f]){2}/p'
