// Source: w3resource.com/javascript-exercises
// Finding sub-strings of a given string

var str = "dog";
var subStrArr = [];
for (let i = 0; i < str.length; i++)
{
  let s = "";
  for (let j = i; j < str.length; j++)
  {
    s += str[j];
    subStrArr.push(s);
  }
}
console.log(`* String: ${str}`);
console.log("* Sub-string array:", subStrArr);

/* Output:

* String: dog
* Sub-string array: [ 'd', 'do', 'dog', 'o', 'og', 'g' ]

*/
