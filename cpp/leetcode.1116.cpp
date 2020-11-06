class ZeroEvenOdd {
private:
    int n;
    std::atomic<int> index;
    std::mutex mtx;
    std::condition_variable cv;
    
public:
    ZeroEvenOdd(int n) {
        this->n = n;
        this->index.store(0);
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        std::unique_lock<std::mutex> uni_lock(mtx);
        while (1)
        {
            cv.wait(uni_lock, [&](){return index.load() >= 2 * this->n || index.load() % 2 == 0;});
            if(index.load() >= 2 * this->n) return;
            if(index.load() % 2 == 0){
                printNumber(0);
                index++;
            }
            cv.notify_all();
        }
    }

    void even(function<void(int)> printNumber) {
        std::unique_lock<std::mutex> uni_lock(mtx);
        while (1)
        {
            cv.wait(uni_lock, [&](){return index.load() >= 2 * this->n || index.load() % 4 == 3;});
            if(index.load() >= 2 * this->n) return;
            if(index.load() % 4 == 3){
                printNumber((index.load() + 1) / 2);
                index++;
            }
            cv.notify_all();
        }
    }

    void odd(function<void(int)> printNumber) {
        std::unique_lock<std::mutex> uni_lock(mtx);
        while (1)
        {
            cv.wait(uni_lock, [&](){return index.load() >= 2 * this->n || index.load() % 4 == 1;});
            if(index.load() >= 2 * this->n) return;
            if(index.load() % 4 == 1){
                printNumber((index.load() + 1) / 2);
                index++;
            }
            cv.notify_all();
        }
    }
};