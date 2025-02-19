/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
    arr1.sort((a, b) => a.id - b.id);
    arr2.sort((a, b) => a.id - b.id);
    let joinedArr = [];
    let i = 0, j = 0;

    while (i < arr1.length && j < arr2.length) {
        if (arr1[i].id < arr2[j].id) {
            joinedArr.push(arr1[i]);
            i++;
        }
        else if (arr2[j].id < arr1[i].id) {
            joinedArr.push(arr2[j]);
            j++;
        }
        else {
            for (const property in arr2[j]) {
                arr1[i][property] = arr2[j][property];
            }
            joinedArr.push(arr1[i]);
            i++;
            j++;
        }
    }

    while (i < arr1.length) {
        joinedArr.push(arr1[i]);
        i++;
    }
    while (j < arr2.length) {
        joinedArr.push(arr2[j]);
        j++;
    }

    return joinedArr;

};