class ProductOfNumbers {
public:
    vector<int> prefProduct = {1};
    int size = 0;
    ProductOfNumbers() {}

    void add(int num) {
        if (num == 0) {
            prefProduct = {1};
            size = 0;
        } else {
            prefProduct.push_back(prefProduct.back() * num);
            size++;
        }
    }

    int getProduct(int k) {
        if (k > size) {
            return 0;
        }
        return prefProduct.back() / prefProduct[size - k];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */