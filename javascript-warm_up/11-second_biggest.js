#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x));
if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)];
  if (uniqueArgs.length <= 1) {
    console.log(0);
  } else {
    uniqueArgs.sort((a, b) => b - a);
    console.log(uniqueArgs[1]);
  }
}
