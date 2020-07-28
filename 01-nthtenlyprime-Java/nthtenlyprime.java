// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

import java.util.*;

class nthtenlyprime {

	public static boolean isPrime(int n) {

		int count = 0;

		for(int i = 1; i <= n; i++) {

			if(n % i == 0) {

				count++;
			}
		}
		return count == 2;
	}

	public boolean istenly(int n) {

		int sum = 0;

		while(n != 0) {

			sum = sum + n % 10;

			n = n / 10;
		}

		if (sum == 10) {

			return true;
		} else {

			return false;
		}
	}
	public int fun_nthtenlyprime(int n){

		List<Integer> al = new ArrayList<Integer>();

		for(int i = 0; i < 3000; i++) {

			if(isPrime(i) && istenly(i)) {

				al.add(i);
			}
		}

		return al.get(n);

	}

	public static void main(String [] args) {

	}
}