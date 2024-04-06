function isAnagram(str1, str2) {
    const cleanStr1 = str1.replace(/[^a-z0-9]/gi, '').toLowerCase();
    const cleanStr2 = str2.replace(/[^a-z0-9]/gi, '').toLowerCase();
    const sortedStr1 = cleanStr1.split('').sort().join('');
    const sortedStr2 = cleanStr2.split('').sort().join('');
    return sortedStr1 === sortedStr2;
}
console.log(isAnagram("Astronomer", "Moon starer")); // Output: true
console.log(isAnagram("School master", "The classroom")); // Output: true
console.log(isAnagram("The Morse Code", "Here come dots")); // Output: true
console.log(isAnagram("Hello", "World")); // Output: false
