import java.util.ArrayList;
import java.util.Scanner;

public class Tungcul_LabAct6 {

    static class Binary_Tree {
        int[] tree_input = new int[10];
        int current_index = 0;

        public void insert(int key) {
            if (current_index < 10) {
                tree_input[current_index++] = key;
            }
        }

        public ArrayList<Integer> preorder_tree_traversal(int index) {
            ArrayList<Integer> result = new ArrayList<>();
            if (index < current_index && tree_input[index] != 0) {
                result.add(tree_input[index]);
                result.addAll(preorder_tree_traversal(2 * index + 1));
                result.addAll(preorder_tree_traversal(2 * index + 2));
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Binary_Tree binary_tree = new Binary_Tree();

        System.out.println("Please enter 10 unique integers between 1 and 100 only:\n=======================================================");

        for (int i = 0; i < 10; i++) {
            int user_input;
            boolean isDuplicate;
            do {
                System.out.print("Enter integer #" + (i + 1) + ": ");
                user_input = scanner.nextInt();

                if (user_input <= 0 || user_input > 100) {
                    System.out.println("Invalid input. Please enter a number between 1 and 100 only.");
                    isDuplicate = true;  
                }
                else {
                    isDuplicate = false;
                    for (int j = 0; j < binary_tree.current_index; j++) {
                        if (binary_tree.tree_input[j] == user_input) {
                            System.out.println("Duplicate/Repeated values are not allowed. Please enter a unique number.");
                            isDuplicate = true;
                            break;  
                        }
                    }
                }
            } 
            while (isDuplicate);

            binary_tree.insert(user_input);
        }

        System.out.println("=======================================================\nPreorder Tree Traversal:");
        ArrayList<Integer> preorder_result = binary_tree.preorder_tree_traversal(0);

        System.out.print("[");
        for (int i = 0; i < preorder_result.size(); i++) {
            System.out.print(preorder_result.get(i));
            if (i < preorder_result.size() - 1) {
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }
}
