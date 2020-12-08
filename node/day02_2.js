const fs = require('fs');

const data = fs.readFileSync('../data/input02.txt').toString('utf-8');
const lines = data.split('\n');

const valid = [];

function isValid(line) {
    if (!line) {
        return;
    }

    const password = line.split(':')[1].trim();
    const first = parseInt(line.split('-')[0]) - 1;
    const second = parseInt(line.split('-')[1].split(' ')[0]) - 1;
    const char = line.split(':')[0].split(' ')[1];

    if ((password[first] === char) !== (password[second] === char)) {
        valid.push(1);
    }
}

lines.forEach(isValid);
console.log(valid.length);
