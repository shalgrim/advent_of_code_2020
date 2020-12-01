const fs = require('fs');

const data = fs.readFileSync('../data/input01.txt').toString('utf-8');
const stringNums = data.split('\n');
const nums = stringNums.map(x => parseInt(x));

let found = false;
let firstNum, secondNum, thirdNum;
for (let i = 0; i < nums.length; ++i) {
    firstNum = nums[i];
    for (let j = i + 1; j < nums.length; ++j) {
        secondNum = nums[j];

        for (thirdNum of nums.slice(j + 1)) {

            if (firstNum + secondNum + thirdNum === 2020) {
                found = true;
                break;
            }
        }

        if (found) {
            break;
        }
    }
    if (found) {
        break;
    }
}

console.log(firstNum * secondNum * thirdNum);
