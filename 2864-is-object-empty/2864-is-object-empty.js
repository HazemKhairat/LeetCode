/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
    // console.log(JSON.stringify(obj).length);
    return JSON.stringify(obj).length == 2;
};