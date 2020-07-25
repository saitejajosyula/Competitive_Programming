// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

import java.util.*;
 
class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){

		Stack<Character> stack = new Stack<>();

		boolean flag = true;

		for(int i = 0; i <s.length(); i++) {

			char c = s.charAt(i);

			if(c == '(' && flag) {

				stack.push(c);
			} else if(c == '(' && !flag) {

				return false;
			} else if(c == ')') {

				flag = false;

				if(!stack.empty()) {

					stack.pop();
				} else{

					return false;
				}
 			}
		}

		if(!stack.empty()) {

			return false;
		}
		return true;	
	}

	public static void main(String[] args) {
		
	}
}
	