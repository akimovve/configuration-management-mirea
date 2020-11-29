import java.util.Scanner;
import java.util.Arrays;

/**
 * \file Main.java
 * Главный класс
 */
public class Main {

	/**
	 * \callgraph
	 * Функция запуска программы
	 * @param args Входные аргументы
	 */
	public static void main(String[] args) {
		System.out.println("Тестирование деревьев...");
		BinaryTree<Integer> binaryTree = new BinaryTree<>();
		Tree<Integer> avlTree = new AvlTree<>();
		System.out.print("Бинарное дерево поиска. Введите количество узлов: ");
		test(binaryTree);
		System.out.print("AVL-дерево. Введите количество узлов: ");
		test(avlTree);
		binaryTree.getSortedArray().forEach(System.out::println);
	}

	/**
	 * \callgraph
	 * Метод тестирования деревьев
	 * @param tree Список деревьев
	 */
	private static void test(Tree<Integer> tree) {
		// int[] testArray = {11, 25, 21, 6, 4, 9, 67, 33, 6};
		// int[] testArray = {1, 25, 26, 27, 4, 67, 33};
		// int[] testArray = {6, 12, 14, 13, 16, 2, 3, 1, 25, 26, 10, 4, 20, 7};
		Scanner scanner = new Scanner(System.in);
		int len = scanner.nextInt();
		for (int i = 0; i < len; i++) {
			tree.addNode(scanner.nextInt());
			tree.print();
		}

		// Arrays.stream(testArray).forEach(tree::addNode);
		// tree.addNode(15, 67, 1);
		// System.out.println("\n\n\nИзначальное дерево...\n");
		tree.print();
		// tree.remove(6);
		// tree.remove(2);
		// System.out.println("\n\nПосле удаления элементов...\n");
		// tree.print();
	}
}
