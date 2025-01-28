/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
    tmp = init;
    var increment = function () {
        return ++tmp;
    }

    var decrement = function () {
        return --tmp;
    }

    var reset = function () {
        tmp = init;
        return tmp;
    }

    return {
        increment,
        decrement,
        reset
    }

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */