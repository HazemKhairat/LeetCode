/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
    // console.log(JSON.stringify(obj).length);
    // console.log(Object.keys(obj).length); 
    for (var item in obj) {
        return false;
    }
    return true;
    // return JSON.stringify(obj).length == 2;
};