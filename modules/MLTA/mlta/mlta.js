#!/usr/bin/env node

var program = require('commander');

program
    .version('0.0.1')
    .command('record', 'Record results from a test')
    .command('config', 'Setup')
    .parse(process.argv);
