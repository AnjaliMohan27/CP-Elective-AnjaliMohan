// Write the method vowelCount(s), that takes a string s, 
// and returns the number of vowels in s, ignoring case, 
// so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).

public class MyString {
    public int vowelCount(String s) {
        int count = 0;
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count = count + 1;
            }
        }
        return count;
    }

}