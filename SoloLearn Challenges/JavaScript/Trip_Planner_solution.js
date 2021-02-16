/* 
You need to plan a road trip. 
You are traveling at an average speed of 40 miles an hour. 
Given a distance in miles as input (the code to take input is already present), 
output to the console the time it will take you to cover it in minutes.
*/

const speed = 40;
const min = 60

function main() {
    
    var distance = parseInt(readLine(), 10);
    console.log(distance / speed * min)
    
}