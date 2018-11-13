#!/bin/bash
ls|sed -n '/.*/p'|wc -l
