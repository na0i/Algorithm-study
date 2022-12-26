nums = [7, 2, 5, 10, 8];
k = 2;
// nums = [1, 2, 3, 4, 5]
// k = 2

const min_sum = Math.max(...nums);
const max_sum = nums.reduce((sum, now) => sum + now, 0);
let mid = (min_sum + max_sum) / 2;

console.log(mid);
