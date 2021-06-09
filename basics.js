// variables
// can declare and assign separately
console.log('js loaded')
let myVariable
const myConstant = "constant"

myVariable = 3;

function compare (number1, number2)  {
    if (number1 > number2) {
        console.log("The first number is higher.")
    }
    else if (number2 > number1) {
        console.log("The second number is higher.")
    }
    else {
        console.log("These numbers are equal.")
    };
};

compare(16, 16)
