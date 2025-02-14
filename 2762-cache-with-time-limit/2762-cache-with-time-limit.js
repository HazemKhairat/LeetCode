class TimeLimitedCache {
    cashe;
    constructor() {
        this.cashe = new Map();
    }

    set(key, value, duration) {
        let found = this.cashe.has(key); // false
        if (found) {
            clearTimeout(this.cashe.get(key).timeOutId);
        }
        const timeOutId = setTimeout(() => this.cashe.delete(key), duration)
        this.cashe.set(key, { value, timeOutId });
        return found;

    };

    get(key) {
        return this.cashe.has(key) ? this.cashe.get(key).value : -1;
    };

    count() {
        return this.cashe.size;
    };
}


const timeLimitedCache = new TimeLimitedCache()
timeLimitedCache.set(1, 42, 1000); // false
timeLimitedCache.get(1) // 42
timeLimitedCache.count() // 1
