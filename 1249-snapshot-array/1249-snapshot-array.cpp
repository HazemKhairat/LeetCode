class SnapshotArray {
public:
    int snap_id;
    vector<vector<pair<int, int>>> snaps;
    SnapshotArray(int len) {
        snap_id = 0;
        snaps.resize(len);
        for (int i = 0; i < len; i++) {
            snaps[i].push_back({0, 0});
        }
    }

    void set(int index, int val) {
        if (!snaps[index].empty() && snap_id == snaps[index].back().first) {
            snaps[index].pop_back();
        }
        snaps[index].push_back(make_pair(snap_id, val));
    }

    int snap() {
        snap_id++;
        return snap_id - 1;
    }

    int get(int index, int snap_id) {
        auto it = upper_bound(snaps[index].begin(), snaps[index].end(),
                              make_pair(snap_id, INT_MAX));
        return prev(it)->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */