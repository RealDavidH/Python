// /*
//   String: Is Palindrome
//   Create a function that returns a boolean whether the string is a strict palindrome.
//     - palindrome = string that is same forwards and backwards

//   Do not ignore spaces, punctuation and capitalization
//  */

//   const str1 = "a x a";
//   const expected1 = true;

//   const str2 = "racecar";
//   const expected2 = true;

//   const str3 = "Dud";
//   const expected3 = false;

//   const str4 = "oho!";
//   const expected4 = false;

// }
// console.log(reversingArr(str1));
// console.log(reversingArr(str2));
// console.log(reversingArr(str3));
// console.log(reversingArr(str4));

//   /**
//    * Determines if the given str is a palindrome (same forwards and backwards).
//    * - Time: O(?).
//    * - Space: O(?).
//    * @param {string} str
//    * @returns {boolean} Whether the given str is a palindrome or not.
//    */

//   ************************************

/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided,
  but also at the substrings within it.
  Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

const two_str1 = "what up, daddy-o?";
const two_expected1 = "dad";

const two_str2 = "uh, not much";
const two_expected2 = "u";

const two_str3 = "Yikes! my favorite racecar erupted!";
const two_expected3 = "e racecar e";

const two_str4 = "a1001x20002y5677765z";
const two_expected4 = "5677765";

const two_str5 = "a1001x20002y567765z";
const two_expected5 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */

function longestPalindromicSubstring(str) {
    let longeststring = "";

    longeststring = findpall(str);
    console.log(longeststring, "end");
}
longestPalindromicSubstring(two_str1);
longestPalindromicSubstring(two_str2);
longestPalindromicSubstring(two_str3);
longestPalindromicSubstring(two_str4);
longestPalindromicSubstring(two_str5);
function findpall(string) {
    let highscore = "";
    let temp = null;
    for (let k = 0; k < string.length; k++) {
        let newstring = "";
        for (let i = 0; i < string.length; i++) {
            newstring += string[i + k];
            for (let j = 0; j < string.length; j++) {
                temp = reversingString(newstring);
                if (temp) {
                    if (newstring.length > highscore.length)
                        highscore = newstring;
                }
            }
        }
    }
    return highscore;
}

function reversingString(str) {
    let j = str.length - 1;
    let tempstr1 = "";
    let tempstr2 = "";

    for (let i = 0; i < str.length / 2; i++) {
        let temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        tempstr1 += str[i];
        tempstr2 += str[j];
        j--;
    }

    if (tempstr2 == tempstr1) {
        return true;
    } else {
        return false;
    }
}
