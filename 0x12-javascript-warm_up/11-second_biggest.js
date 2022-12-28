#!/usr/bin/node

const nums = process.argv.slice(2).map(
  function (arg) {
    return (parseInt(arg));
  }
);

nums.sort(function (a, b) { return a - b; });

if (nums.length === 0 || nums.length === 1) {
  console.log(0);
} else {
  console.log(nums[nums.length - 2]);
}
