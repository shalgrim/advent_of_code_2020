const fs = require('fs');

const data = fs.readFileSync('../data/input02.txt').toString('utf-8');
const lines = data.split('\n');

const valid = [];

function isValid(line) {
    if (!line) {
        return;
    }

    const password = line.split(':')[1].trim();
    const lo = parseInt(line.split('-')[0]);
    const hi = parseInt(line.split('-')[1].split(' ')[0]);
    const char = line.split(':')[0].split(' ')[1];

    let count = 0;

    for (c of password) {
        if (c === char) {
            count++;
        }
    }

    if (count >= lo && count <= hi) {
        valid.push(1);
    }
}

lines.forEach(isValid);
let numValid = 0;

console.log(valid.length);
