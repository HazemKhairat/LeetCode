class NumberContainers {
public:
    map<int, int> idxs;
    map<int, set<int>> nums;
    NumberContainers() {}

    void change(int index, int number) {
        if (idxs.count(index)) {
            nums[idxs[index]].erase(index);
            if (nums[idxs[index]].empty()) {
                nums.erase(idxs[index]);
            }
        }
        idxs[index] = number;
        nums[number].insert(index);
    }

    int find(int number) {
        if (nums.count(number)) {
            return *nums[number].begin();
        } else {
            return -1;
        }
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */