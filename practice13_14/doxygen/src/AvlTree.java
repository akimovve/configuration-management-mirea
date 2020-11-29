/**
 * \file AvlTree.java
 * Класс АВЛ дерева
 * @param <T> Дженерик для универсальности данных, хранимых в дереве
 */
public class AvlTree<T extends Comparable<T>> extends Tree<T> {

	/**
	 * Пустой конструктор дерева
	 */
	public AvlTree() {}

	/**
	 * \callgraph
	 * Конструктор дерева
	 * @param value Элемент дерева
	 */
	public AvlTree(T value) {
		super(value);
	}

	/**
	 * \callgraph
	 * Добавление элемента в АВЛ дерево
	 * @param node Узел для добавления
	 * @param value Элемент для добавления
	 * @return Узел, добавленный в дерево
	 */
	@Override
	protected Node insertNode(Node node, T value) {
		return balance(super.insertNode(node, value));
	}

	/**
	 * \callgraph
	 * Функция удаления узла из АВЛ дерева
	 * @param node Узел, из которого происходит удаление
	 * @param value Элемент, который необходимо удалить
	 * @return Узел
	 */
	@Override
	protected Node remove(Node node, T value) {
		return balance(super.remove(node, value));
	}

	/**
	 * \callgraph
	 * Обновление значения высоты ветви
	 * @param node Узел для проверки
	 */
	private void updateBranchHeight(Node node) {
		node.height = Math.max(getBranchHeight(node.left), getBranchHeight(node.right)) + 1;
	}

	/**
	 * Получение высоты ветви
	 * @param node Узел
	 * @return Высота
	 */
	private int getBranchHeight(Node node) {
		return (node == null) ? -1 : node.height;
	}

	/**
	 * \callgraph
	 * Сопоставление длин высот ветвей дерева
	 * @param node Узел
	 * @return Разность высот
	 */
	private int compareBranchesLength(Node node) {
		return (node == null) ? 0 : getBranchHeight(node.right) - getBranchHeight(node.left);
	}

	/**
	 * \callgraph
	 * Балансировка ветвей для АВЛ-дерева
	 * @param node Узел
	 * @return Узел
	 */
	private Node balance(Node node) {
		if (node == null)
			return null;
		updateBranchHeight(node);
		int difference = compareBranchesLength(node);

		if (difference == 0 || Math.abs(difference) == 1)
			return node;

		// Левое вращение
		if (difference > 1) {
			if (getBranchHeight(node.right.right) <= getBranchHeight(node.right.left)) {
				node.right = rightRotate(node.right);
			}
			return leftRotate(node);
		}

		// Правое вращение
		if (getBranchHeight(node.left.left) <= getBranchHeight(node.left.right)) {
			node.left = leftRotate(node.left);
		}
		return rightRotate(node);
	}

	/**
	 * \callgraph
	 * Левый поворот
	 * @param node Узел
	 * @return Узел
	 */
	private Node leftRotate(Node node) {
		Node right = node.right;
		Node left = right.left;
		right.left = node;
		node.right = left;
		updateBranchHeight(node);
		updateBranchHeight(right);
		return right;
	}

	/**
	 * \callgraph
	 * Правый поворот
	 * @param node Узел
	 * @return Узел
	 */
	private Node rightRotate(Node node) {
		Node left = node.left;
		Node right = left.right;
		left.right = node;
		node.left = right;
		updateBranchHeight(node);
		updateBranchHeight(left);
		return left;
	}
}
