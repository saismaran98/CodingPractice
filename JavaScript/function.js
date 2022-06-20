/*  
    Named Function i.e function functionName(){}
    function expression: qty=parameter, parameter are value/variable which function can access during its runtime. 
    hoising will first run or equivalent to putting code on this line as const loaves=makeBread(); 
    function declaration:
    const loaves= makeBread(7); //works as hoisting will bring it up anyways to global namespace 
*/
function makeBread(qty){
    const bread = '🍞'.repeat(7);
    return bread; //return bread
}

//function call: (7)=args
const loaves= makeBread(7); //here when i call makeBread js is able to recognize as function body is at the top, it is also 
//good practice to write all var/function var at the top. hoisting would take the code to the top
console.log(loaves); //prints 🍞🍞🍞🍞🍞🍞🍞

//anonymous function i.e (function ()=>{}) 
//function expression: these are var assigned anonymous functions, these are not hoisted and wont pollute global namespace.  
const makeBeer = function(qty) {
    return '🍺';
}
//Array Syntax for above function:
const makeWine= (qty) => '🍷'.repeat(qty)   //similar to lambda function in Java8, more than one line logic we can add {} and return a value.  

//IIFE: Immidiately invoked function expression, wrapping anonymous function in paranthesis and calling immidiately. 
(function () {
    const x = 23;
}()); //called immidiately by adding ()

//Parameters and arguments
//Rest Params
function makeDinner(...args){ // ... is telling js that its an array of args. so we can pass as many on an array. 
    return `Dinner include items: ${args.json}` 
}
makeDinner('🥐','🥑','🥗','🦐');

//Pure Functions
const pureFunc= (x) => x ** 2; // exponentiation operator ( ** )
//impure function
let x=4;
const impureFunc= (x)=> x**2;  
/* 
 pure function only mutate/modify variable in their local scope and allow us to compose our function as
 higher order functions.(HOF)
 HOF()= function that can take other function as their input args or return a new function when called. ex. async or setTimeout
 Impure functions are functions which modify and operates on variables outside its local scope, ex. global vars. 
 
 */
//.map() we can use inplace of for loops, 
const arr= [1,2,3,4];
const squared=[];
/*
for (const x of arr){
    squared.push(x**2);
}
*/
const squared=arr.map(x => x**2); //using .map() and arrow functions

//Closures
const a = 1;
//lexical env a 
const outer = () => {
const b=2 //lexical env b, here we can access above lexical envs. not below
    const inne=(message)=>{
        const c=3; //lexical env c, here we can access var in lexical env a, b, c
        return a+b+c
    }
}

//Recursion
const theMeaningOfLife=()=>{
    if(theMeaningOfLife()){
        theMeaningOfLife();
    }
    else{
        return 0;
    }
}