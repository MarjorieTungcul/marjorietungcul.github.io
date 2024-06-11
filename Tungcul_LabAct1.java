import java.util.Scanner;

public class Tungcul_LabAct1 {
    public static int balance = 10000;
    public static int withdraw;
    public static void main(String[] args) {
        Scanner user_input= new Scanner(System.in);

        while (true) {
            displayMenu();
            int choice = user_input.nextInt();

            switch (choice) {
                case 1:
                    balance();
                    break;
                case 2:
                    withdraw(user_input);
                    break;
                case 3:
                    exit();
                    return; 
                default:
                    System.out.println("Incorrect input. Please try again. \n============================================================");
            }
        }
    }

    public static void displayMenu() {
        System.out.println("Welcome to the Automated Teller Machine! To transact, type: \n1 - Check balance \n2 - Withdraw \n3 - Exit ");
        System.out.print("Transaction number: ");
    }

    public static void balance() {
        System.out.printf("Your current balance is PHP %d. %n============================================================ %n", balance);
    }

    public static void withdraw(Scanner user_input) {
      while (true) {
        System.out.print("Please type in the amount you want to withdraw: ");
        int withdrawalAmount = user_input.nextInt();

        if (withdrawalAmount <= balance) {
          int thousands = withdrawalAmount / 1000;
          withdrawalAmount %= 1000;
          int hundreds = withdrawalAmount / 100;
          withdrawalAmount %= 100;
          int twenties = withdrawalAmount / 20;
          withdrawalAmount %= 20;
          int coins = withdrawalAmount / 1;

          withdraw = (thousands * 1000 + hundreds * 100 + twenties * 20 + coins);
          System.out.printf("You have withdrawn PHP %d. Here is the denomination of bills: %nPHP 1000: %d %nPHP 100: %d %nPHP 20: %d %nCoins: %d %n============================================================ %n", withdraw, thousands, hundreds, twenties, coins);
 
          balance -= (thousands * 1000 + hundreds * 100 + twenties * 20 + coins);
          break;
        }
        else if (balance == 0) {
          System.out.println("Sorry, but your account balance is currently zero. You cannot perform withdrawals at the moment. \n============================================================");
          break;
        } 
        else {
            System.out.println("The amount is greater than your current balance. Please try again.");
        }
      }
    }
    public static void exit() {
        System.out.println("Thank you for using our ATM!");
    }
}
