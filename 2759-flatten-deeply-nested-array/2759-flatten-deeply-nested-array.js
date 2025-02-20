/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const res = [];
    for (var item of arr) {
        if (Array.isArray(item) && n > 0) {
            res.push(...flat(item, n - 1));
        }
        else res.push(item);
    }
    return res;
};

// var recuris = function (arr, res, depth, n) {
//     for (const item of arr) {
//         if (Array.isArray(item) && depth < n) {
//             recuris(item, res, depth + 1, n);
//         }
//         else {
//             res.push(item);
//         }
//     }
// }