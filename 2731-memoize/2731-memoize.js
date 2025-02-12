/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const memo = new Map();
    return function (...args) {
        // console.log(args);
        const key = JSON.stringify(args);
        // console.log(key);
        if (memo.has(key)) {
            return memo.get(key);
        }
        const res = fn(...args);
        memo.set(key, res);
        return res;

    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */