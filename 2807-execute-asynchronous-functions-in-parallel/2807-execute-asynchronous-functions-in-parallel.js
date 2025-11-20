/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
    let count = 0
    res = new Array(functions.length).fill(null)
    return new Promise((resolve, reject) => {
        functions.forEach(
            async (fun, idx) => {
                try {
                    res[idx] = await fun()
                    count++
                    if (count == functions.length) {
                        resolve(res)
                    }
                }
                catch (error) {
                    reject(error)
                }
            }
        )
    })

};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */