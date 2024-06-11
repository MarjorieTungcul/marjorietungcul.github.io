import java.util.*;

public class Tungcul_LabAct9 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.print("Enter the number of vertices: ");
        int num_of_vertices = scanner.nextInt();
        Graph my_graph = new Graph(num_of_vertices);
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

        for (int i = 0; i < num_of_vertices; i++) {
            System.out.print("Enter node data for node " + (i + 1) + ": ");
            char my_node_data = scanner.next().charAt(0);
            my_graph.addNode(new Node(my_node_data));
        }
        
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("NOTE: For entering edges, use format: vertex_index 1 [space] vertex_index 2. For example: 1 2.");
        while (true) {
            System.out.print("Enter edges (type 'end' to finish): ");
            String srcInput = scanner.next();
            if (srcInput.equalsIgnoreCase("end"))
                break;
            String dstInput = scanner.next();
            if (dstInput.equalsIgnoreCase("end"))
                break;

            int src, dst;
            if (Character.isDigit(srcInput.charAt(0))) {
                src = Integer.parseInt(srcInput) - 1; 
                dst = Integer.parseInt(dstInput) - 1; 
            } else {
                src = (int) srcInput.charAt(0) - 'A'; 
                dst = (int) dstInput.charAt(0) - 'A'; 
            }

            if (src < 0 || src >= num_of_vertices || dst < 0 || dst >= num_of_vertices) {
                System.out.println("Invalid vertex index. Please enter valid indices within the range [1, " + num_of_vertices + "].");
                continue;
            }
            my_graph.addEdge(src, dst);
        }

        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("Here is the Adjacency Matrix:");
        my_graph.print();

        KruskalAlgorithm my_kruskal_algorithm = new KruskalAlgorithm(my_graph);
        my_kruskal_algorithm.kruskalMST();
        
        while (true) {
            System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            System.out.println("Do you want to try again? (Y/y/N/n)");
            String tryAgain = scanner.next();
            if (tryAgain.equalsIgnoreCase("Y")) {
                main(args);
                break; 
            } else if (tryAgain.equalsIgnoreCase("N")) {
                System.out.println("Program exited.");
                scanner.close();
                return; 
            } else {
                System.out.println("Invalid input. Please enter 'Y', 'y', 'N', or 'n'.");
            }
        }        
    }
}

class Edge implements Comparable<Edge> {
    int source, destination, weight;

    public int compareTo(Edge compareEdge) {
        return this.weight - compareEdge.weight;
    }
}

class KruskalAlgorithm {
    private Graph my_graph;

    KruskalAlgorithm(Graph my_graph) {
        this.my_graph = my_graph;
    }

    int find(int[] parent, int i) {
        if (parent[i] == -1)
            return i;
        return find(parent, parent[i]);
    }

    void union(int[] parent, int x, int y) {
        int xset = find(parent, x);
        int yset = find(parent, y);
        parent[xset] = yset;
    }

    void kruskalMST() {
        ArrayList<Edge> result = new ArrayList<>();
        int V = my_graph.nodes.size();
        int[] parent = new int[V];
        Arrays.fill(parent, -1);

        ArrayList<Edge> edges = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (my_graph.checkEdge(i, j)) {
                    Edge edge = new Edge();
                    edge.source = i;
                    edge.destination = j;
                    edge.weight = 1; 
                    edges.add(edge);
                }
            }
        }

        Collections.sort(edges);

        int e = 0;
        int i = 0;
        int min_cost = 0; 
        while (e < V - 1 && i < edges.size()) {
            Edge nextEdge = edges.get(i++);
            int x = find(parent, nextEdge.source);
            int y = find(parent, nextEdge.destination);
            if (x != y) {
                result.add(nextEdge);
                union(parent, x, y);
                e++;
                min_cost += nextEdge.weight; 
            }
        }

        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("Here is the Computed Minimum Cost of the Spanning Tree: " + min_cost); 
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("Here are the Edges of the Minimum Cost Spanning Tree:");
        for (Edge edge : result) {
            System.out.println(my_graph.nodes.get(edge.source).my_node_data + " - " + my_graph.nodes.get(edge.destination).my_node_data);
        }
    }
}

class Graph {

    ArrayList<Node> nodes;
    int[][] matrix;

    Graph(int size) {
        nodes = new ArrayList<>();
        matrix = new int[size][size];
    }

    public void addNode(Node node) {
        nodes.add(node);
    }

    public void addEdge(int src, int dst) {
        matrix[src][dst] = 1;
        matrix[dst][src] = 1; 
    }

    public boolean checkEdge(int src, int dst) {
        return matrix[src][dst] == 1;
    }

    public void print() {
        System.out.print("   ");
        for (Node node : nodes) {
            System.out.printf("%2c ", node.my_node_data);
        }
        System.out.println();

        for (int i = 0; i < matrix.length; i++) {
            System.out.printf("%2c ", nodes.get(i).my_node_data);
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf("%2d ", matrix[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
}

class Node {

    char my_node_data;

    Node(char my_node_data) {
        this.my_node_data = my_node_data;
    }
}
