/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {

    function dfs(obj) {
        if (!obj)
            return false;
        else if (typeof obj != 'object')
            return obj;
        else if (Array.isArray(obj)) {
            const newArr = [];
            for (var i = 0; i < obj.length; i++) {
                let curr = dfs(obj[i]);
                if (curr) {
                    newArr.push(curr);
                }
            }
            return newArr;
        }
        else {
            const newObj = {};
            for (var key in obj) {
                let curr = dfs(obj[key]);
                if (curr) {
                    newObj[key] = curr;
                }
            }
            return newObj;
        }


    }

    return dfs(obj);

};