/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const res = [];
    recuris(arr, res, 0, n);
    return res;
};

var recuris = function (arr, res, depth, n) {
    for (const item of arr) {
        if (Array.isArray(item) && depth < n) {
            recuris(item, res, depth + 1, n);
        }
        else {
            res.push(item);
        }
    }
}