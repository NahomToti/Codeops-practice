// function myfun(){
//     let x=10
//     console.log("hello class")
// }

// console.log(myfun())



// greet("Abebe", "Kebede");

// function greet(...params){
//     console.log(`Good afternoon ${params[0]} ${params[1]}`);
// }

//   const greet = function outer(){
//       let student = "Abebe"; //private



//       const inner = () =>{
//          console.log(student);
//       };
//       inner();
//   };

//   greet();

// function mynumber(){
//   let number = 0;
 
//   return{
//     next(){ number--; return number;},
//     current(){return number;}
//   };
// } 
// console.log(mynumber);

// const bank = (mynumber);
 

function adder(num1 , num2 , fun){

console.log(fun(num1 ,num2))
 fun(num1 , num2)
}


function sum(a,b){
    return a+b
}

sum(10,20)

console.log(adder (10,20 , sum))

function substractor(a,b){

}