// class Solution {
//     public int mySqrt(int x) {
//         int l = 1;
//         int r = x;

//         while(l <= r){
//             int mid = (l + r) / 2;

//             if(x / mid == mid){
//                 return mid;
//             } else if(mid > x / mid){
//                 r = mid - 1;
//             } else {
//                 l = mid + 1;
//             }
//         }

//         return r;
//     }


//     public static void main(String[] args) {
//         Solution solution = new Solution();
//         int x = 16; // test value for square root
//         int result = solution.mySqrt(x);
//         System.out.println("The square root of " + x + " is: " + result);
//     }
    
// }




// import java.util.Scanner;

// class Solution {
//     public int rumor(String cantidades,String gold) {

//         String[] sociales = new String[cantidades.length()];
//         for (int i = 0; i < cantidades.length(); i++) {
        

//             Scanner scanner = new Scanner(System.in);
//             String friends = scanner.nextLine();
//             friends.trim().split("\\s+");
//             sociales.add(friends[1]);
//             scanner.close();
//         }
//         suma = 0
//         for i in range(1,int(cantidades[0])+1):
//             if str(i) not in sociales:
//                 suma += int(tokenized_gold[int(i)-1])

//         return suma;
//     }

//     public static void main(String[] args) {
//         Solution solution = new Solution();

//         Scanner scanner = new Scanner(System.in);
//         String cantidades = scanner.nextLine();
//         cantidades.trim().split("\\s+");

//         Scanner scanner2 = new Scanner(System.in);
//         String gold = scanner2.nextLine();
//         gold.trim().split("\\s+");

//         int result = solution.rumor(cantidades,gold);
        
//         scanner.close();
//         scanner2.close();

//         System.out.println(result);
//     }
    
// }