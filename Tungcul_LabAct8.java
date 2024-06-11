import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

class My_node {
    int key, height;
    My_node left, right;

    My_node (int d) {
        key = d;
        height = 1;
    }
}

class AVLTree {
    My_node root;
    List<Integer> elements;

    int height(My_node N) {
        if (N == null)
            return 0;
        return N.height;
    }

    int max(int a, int b) {
        return (a > b) ? a : b;
    }

    My_node rightRotate(My_node y) {
        My_node x = y.left;
        My_node T2 = x.right;

        x.right = y;
        y.left = T2;

        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;

        return x;
    }

    My_node leftRotate(My_node x) {
        My_node y = x.right;
        My_node T2 = y.left;

        y.left = x;
        x.right = T2;

        x.height = max(height(x.left), height(x.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;

        return y;
    }

    int getBalance(My_node N) {
        if (N == null)
            return 0;
        return height(N.left) - height(N.right);
    }

    My_node insert(My_node node, int key) {
        if (node == null)
            return (new My_node(key));

        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else
            return node;

        node.height = 1 + max(height(node.left), height(node.right));

        int balance = getBalance(node);

        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    void levelOrder(My_node root) {
        if (root == null)
            return;

        Queue<My_node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            My_node tempNode = queue.poll();
            System.out.print(tempNode.key + " ");

            if (tempNode.left != null)
                queue.add(tempNode.left);

            if (tempNode.right != null)
                queue.add(tempNode.right);
        }
    }

    void preOrder(My_node node) {
        if (node != null) {
            elements.add(node.key);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    void printPreOrder() {
        System.out.println("===============================================================");
        System.out.print("Here are the elements in Preorder Traversal: \n{ ");
        for (int i = 0; i < elements.size(); i++) {
            System.out.print(elements.get(i));
            if (i < elements.size() - 1)
                System.out.print(", ");
        }
        System.out.println(" }");
    }
}

public class Tungcul_LabAct8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AVLTree tree = new AVLTree();
        tree.elements = new LinkedList<>();

        System.out.println("==================== Lab Act 8 -- AVL Tree ====================");
        System.out.println("===============================================================");

        while (true) {
            System.out.print("Please enter 'i' to insert an integer, or 'e' to end the program: ");
            String choice = scanner.next();

            if (choice.contentEquals("e"))
                break;
            else if (choice.contentEquals("i")) {
                System.out.print("Enter an integer value: ");
                if (scanner.hasNextInt()) {
                    int num = scanner.nextInt();
                    tree.root = tree.insert(tree.root, num);
                    System.out.println("Balanced AVL Tree:");
                    tree.levelOrder(tree.root);
                    System.out.println("\n===============================================================");
                } else {
                    System.out.println("Invalid input. Please enter an integer.");
                    scanner.next();
                }
            } else {
                System.out.println("Invalid choice. Please enter 'i' or 'e' only.\n===============================================================");
            }
        }

        tree.preOrder(tree.root);
        tree.printPreOrder();
    }
}
