/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.

  pseudocode
  - create a function that takes in a string
  - 

  */

const str1 = "aaaabbcdddaaa";
const expected1 = "a4b2c1d3a3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbccd";
const expected4 = "bbccd";

function amoutOfNums(string) {
    if (string.length < 3){
        return string
    }
    let amount = 1;
    let tempstr = "";
    let letter = ""
    for (let i = 1; i <= string.length; i++) {
        letter = string.charAt(i-1);
        if (letter == string.charAt(i)) {
            amount++;
        } 
        else if (letter != string.charAt(i)) {
            tempstr += letter + amount
            amount = 1
        }
    }
    if (tempstr.length >= string.length){
        return string
    } else {
    return tempstr
    }
}
console.log(amoutOfNums(str1))
console.log(amoutOfNums(str2))
console.log(amoutOfNums(str3))
console.log(amoutOfNums(str4))



/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) {}

//   *********************************************

/* 
  String Decode  
*/

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {}
