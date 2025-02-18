/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
    return new Promise((resolve, reject) => {
        if (functions.length == 0) {
            resolve([]);
            return;
        }

        let countResolved = 0;
        const res = new Array(functions.length).fill(null);

        functions.forEach((fun, idx) => {
            fun().then((val) => {
                res[idx] = val;
                countResolved++;
                if (countResolved == functions.length) {
                    resolve(res);
                }
            }).catch((error) => {
                reject(error);
            })
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */