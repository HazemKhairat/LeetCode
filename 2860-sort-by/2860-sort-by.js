/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
    // Aproach 1
    // function swap(a, b){
    //     return fn(a) - fn(b);
    // }
    // return arr.sort(swap);
    // =========

    // Aproach 2
    // return arr.sort((a, b) => fn(a) - fn(b));
    // =========

    // Aproach 3
    return arr.sort(function (a, b) {
        return fn(a) - fn(b);
    });
};