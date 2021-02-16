/*
The snail climbs up 7 feet each day and slips back 2 feet each night. 
How many days will it take the snail to get out of a well with the given depth?
*/

function main() {

    var depth = parseInt(readLine(), 10);
    
    var days = 0
    var climb = 0
    
    while (climb <= depth) {
        climb += 7
        days += 1
    
        if (climb >= depth) {
            break;
        }
    
        climb -= 2
    }
    
    console.log(days)
    
    }
    