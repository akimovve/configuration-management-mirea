import java.util.ArrayList;
import java.util.List;

/**
 * \file BinaryTree.java
 * Класс бинарного дерева
 * @param <T> Дженерик для универсальности данных, хранимых в дереве
 */
public class BinaryTree<T extends Comparable<T>> extends Tree<T> {

	/**
	 * Пустой конструктор дерева
	 */
	public BinaryTree() {}

	/**
	 * \callgraph
	 * Конструктор дерева
	 * @param value Элемент дерева
	 */
	public BinaryTree(T value) {
		super(value);
	}

	/**
	 * \callgraph
	 * Составление отсортированного списка из дерева
	 */
	public List<T> getSortedArray() {
		List<T> sortedArray = new ArrayList<>();
		getSortedArray(parent, sortedArray, 0);
		return sortedArray;
	}

	/**
	 * \callgraph
	 * Составление отсортированного массива
	 * @param node Узел
	 * @param list Список для сортировки
	 * @param i Глубина
	 * @return Глубину
	 */
	private int getSortedArray(Node node, List<T> list, int i) {
		if (node.left != null)
			i = getSortedArray(node.left, list, i);
		list.add(i++, node.value);
		if (node.right != null)
			i = getSortedArray(node.right, list, i);
		return i;
	}
}
