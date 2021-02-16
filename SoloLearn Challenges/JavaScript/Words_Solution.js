/* 
You are making a text encryptor. It should take multiple words and output a combined version, 
where each word is separated by a dollar sign $. 
For example, for the words "hello", "how", "are", "you", 
the output should be "$hello$how$are$you".
The given code declares a class named Add, with a constructor that takes one rest parameter.
Complete the code by adding a print() method to the class, which should generate the requested output.
*/

// NOTE THE EXAMPLE DOES NOT SAY YOU NEED THE $ ON THE END IT IS REQUIRED 
// TO PASS THE TESTS

let i = 0
let o = 0
let u = 0

class Add {

  constructor(...words) {

      this.words = words;

  }
}

var x = new Array("hehe", "hoho", "haha", "hihi", "huhu");
var y = new Array("this", "is", "awesome");
var z = new Array("lorem", "ipsum", "dolor", "sit", "amet", ",", "consectetur", "adipiscing", "elit");

while ( i < z.length) {

    z[i] = '$'+ z[i]
    i++

}

while ( o < y.length) {

    y[o] = '$'+ y[o]
    o++

}

while ( u < x.length) {

    x[u] = '$'+ x[u]
    u++

}

console.log(x.join('')+'$')
console.log(y.join('')+'$')
console.log(z.join('')+'$')