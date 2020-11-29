import java.util.Arrays;

/**
 * \file Tree.java
 * Абстрактный класс дерева
 * @param <T> Дженерик для универсальности данных, хранимых в дереве
 */
public abstract class Tree<T extends Comparable<T>> {
	protected Node parent;

	protected class Node {
		protected T value;
		protected Node left;
		protected Node right;
		protected int height;

		/**
		 * Конструктор узла
		 * @param value Элемент дерева
		 */
		public Node(T value) {
			this.value = value;
		}

		@Override
		public String toString() {
			return value.toString();
		}
	}

	/**
	 * Пустой конструктор дерева
	 */
	public Tree() {}

	/**
	 * \callgraph
	 * Конструктор дерева
	 * @param value Элемент дерева
	 */
	public Tree(T value) {
		parent = new Node(value);
	}

	/**
	 * \callgraph
	 * Добавление последовательности элементов в дерево
	 * @param values Последовательность элементов
	 */
	@SafeVarargs
	public final void addNode(T... values) {
		Arrays.stream(values).forEach(this::addNode);
	}

	/**
	 * \callgraph
	 * Добавление одного элемента в дерево
	 * @param value Элемент для добавления
	 */
	public void addNode(T value) {
		parent = insertNode(parent, value);
	}

	/**
	 * \callgraph
	 * Добавление элемента в дерево
	 * @param node Узел для добавления
	 * @param value Элемент для добавления
	 * @return Узел, добавленный в дерево
	 */
	protected Node insertNode(Node node, T value) {
		if (node == null)
			return new Node(value);
		if (node.value.compareTo(value) > 0) {
			node.left = insertNode(node.left, value);
		} else if (node.value.compareTo(value) < 0) {
			node.right = insertNode(node.right, value);
		}
		return node;
	}

	/**
	 * \callgraph
	 * Удаление элемента из дерева
	 * @param value Элемент для удаления из дерева
	 */
	public void remove(T value) {
		parent = remove(parent, value);
	}

	/**
	 * \callgraph
	 * Функция удаления
	 * @param node Узел, из которого происходит удаление
	 * @param value Элемент, который необходимо удалить
	 * @return Узел
	 */
	protected Node remove(Node node, T value) {
		if (node == null || node.left == null && node.right == null)
			return null;
		if (node.value.compareTo(value) > 0) {
			node.left = remove(node.left, value);
			return node;
		}
		if (node.value.compareTo(value) < 0) {
			node.right = remove(node.right, value);
			return node;
		}
		// Только левая ветвь
		if (node.right == null) {
			node = node.left;
			return node;
		}
		// Только правая ветвь
		if (node.left == null) {
			node = node.right;
			return node;
		}
		// Обе ветви => ищем наим. значение в правой ветви
		Node min = minValueInRightBranch(node.right);
		node.value = min.value;
		node.right = remove(node.right, min.value);
		return node;
	}

	/**
	 * \callgraph
	 * Поиск наименьшего числа в левой ветви
	 * @param node Узел для поиска
	 * @return Узел, в котором необходимо искать
	 */
	protected Node minValueInRightBranch(Node node) {
		return (node.left != null) ? minValueInRightBranch(node.left) : node;
	}

	/**
	 * \callgraph
	 * Печать дерева в консоль
	 */
	public void print() {
		printTree(parent, 0);
	}

	/**
	 * \callgraph
	 * Печать дерева
	 * @param node Узел для печати
	 * @param level Глубина дерева
	 */
	private void printTree(Node node, int level) {
		if (node == null)
			return;
		printTree(node.right, level + 1);
		for (int i = 0; i < level; i++) {
			System.out.print("	");
		}
		System.out.println(node + "〈");
		printTree(node.left, level + 1);
	}
}
