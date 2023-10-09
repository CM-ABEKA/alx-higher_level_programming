#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python Lists
 * @p: python object
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, list_len = 0;
	PyObject *item;
	PyListObject *list;

	list_len = Py_SIZE(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) list->allocated);

	for (; i < list_len; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}

	return;
}

