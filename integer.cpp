#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		
		int fib();
	private:
		int val;
		int fibp(int);
	};
 
Integer::Integer(int n){
	val = n;
	}



int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}

int Integer::fib(){
    return fibp(val);
}

int Integer::fibp(int n){
    if(n==0){
         return 0;
         }
        if(n==1){
            return 1;
        }
        if(n==2){
            return 1;
        }
        return fibp(n-1)+fibp(n-2);
    }


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	int Integer fibp(Integer* integer) {return integer->fib()};
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
	