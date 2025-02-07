/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
    var index = 0;
    var res = [];
    while (index < arr.length) {
        var newArr = []
        var tmp = size;
        while (tmp-- && index < arr.length) {
            newArr.push(arr[index]);
            index++;
        }
        res.push(newArr);
    }
    return res;
};
