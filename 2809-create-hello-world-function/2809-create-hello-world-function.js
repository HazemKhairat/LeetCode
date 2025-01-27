/**
 * @return {Function}
 */

var createHelloWorld = function(...args){
    return function(){
        return "Hello World";
    }
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */