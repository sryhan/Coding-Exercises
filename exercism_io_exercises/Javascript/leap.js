// Given a year, report if it is a leap year.
//
// The tricky thing here is that a leap year in the Gregorian calendar occurs:
//
// on every year that is evenly divisible by 4
//   except every year that is evenly divisible by 100
//     unless the year is also evenly divisible by 400
//
// For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.
//
// If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.




function isLeapYear(year) {
  var year;
  if (year % 4 == 0) {
    if (year % 100 == 0) {
      if (year % 400 == 0 ){
        console.log("Leap year")
      }
      console.log("Not a leap year")
    }
    console.log("It is a leap year")
  }
  else if (year % 4 != 0) {
    console.log("Not a leap year")
  }
}
