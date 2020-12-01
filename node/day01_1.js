const fs = require('fs');

const data = fs.readFileSync('../data/input01.txt').toString('utf-8');
const stringNums = data.split('\n');
const nums = stringNums.map(x => parseInt(x));

let found = false;
let firstNum, secondNum;
for (let i = 0; i < nums.length; ++i) {
    firstNum = nums[i];
    for (secondNum of nums.slice(i + 1)) {
        if (firstNum + secondNum === 2020) {
            found = true;
            break;
        }
    }
    if (found) {
        break;
    }
}

console.log(firstNum*secondNum);
