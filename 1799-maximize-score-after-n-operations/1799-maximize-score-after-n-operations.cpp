class Solution {
public:
    // Simple doubly linked list
    class Node {
    public:
        Node() {

        };
        Node (int v, int originalInd, Node* prev, Node* next) {
            this->value = v;
            this->originalInd = originalInd;
            this->prev = prev;
            this->next = next;
        }
        int value;
        // the 0-based index of this value in the given nums array
        int originalInd;
        Node* next = nullptr;
        Node* prev = nullptr;
    };

    int maxScore(vector<int>& nums) {
        // init linked list!
        Node* head = new Node(nums[0], 0, nullptr, nullptr);
        Node* prev = head;
        for (int i = 1;i < nums.size(); ++i) {
            prev->next = new Node(nums[i], i, prev, nullptr);
            prev = prev->next;
        }
        // prepare bitmasking and caching.
        unordered_map<int, int> cache{};
        return recurse(0, head, cache, 0);
    }

    int recurse(int i, Node* choices, unordered_map<int, int>& cache, int mask) {
        // termination conditions
        if (choices == nullptr) {
            return 0;
        } else if (cache.find(mask) != cache.end()) {
            return cache[mask]; // return cache if we calculated before
        }

        int res = 0;
        for (Node* choice1 = choices; choice1 != nullptr; choice1 = choice1->next) {
            for (Node* choice2 = choice1->next; choice2 != nullptr; choice2 = choice2->next) {
                // Calculate the score for this particular choice.
                int thisScore = (i + 1) * gcd(choice1->value, choice2->value);

                // Get the next bit mask.
                int newMask = (1 << choice1->originalInd) | (1 << choice2->originalInd) | mask;

                // Note that choice2.prev will never be nullptr
                // First, we remove choice2 from ll.
                choice2->prev->next = choice2->next;
                if (choice2->next != nullptr)
                    choice2->next->prev = choice2->prev;

                // Next, we remove choice1 from ll.
                if (choice1->next != nullptr)
                    choice1->next->prev = choice1->prev;
                if (choice1->prev == nullptr) {
                    Node* newHead = choice1->next;//skip choice1
                    res = max(res, recurse(i + 1, newHead, cache, newMask) + thisScore);
                } else {
                    choice1->prev->next = choice1->next;//remove choice1
                    res = max(res, recurse(i + 1, choices, cache, newMask) + thisScore);
                    choice1->prev->next = choice1;//put choice1 back.
                }
                if(choice1->next != nullptr)
                    choice1->next->prev = choice1;//put choice1 back

                //put choice2 back
                choice2->prev->next = choice2;
                if (choice2->next != nullptr)
                    choice2->next->prev = choice2;
            }
        }
        cache[mask] = res; // cache this one!
        return res;
    }

    void print_ll(Node* head) {
        for (Node* cur = head; cur != nullptr; cur = cur->next)
            cout << cur->value << " (prev is: " << (cur->prev == nullptr ? -1000 : cur->prev->value) << "), ";
        cout << endl;
    }
};