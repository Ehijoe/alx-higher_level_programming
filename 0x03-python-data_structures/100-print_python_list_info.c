#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <object.h>
#include <listobject.h>

#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Prints information about a python list
 * @p: A pointer to the list object
 */
void print_python_list_info(PyObject *p)
{
	int len, i;

	if (!PyList_Check(p))
	{
		printf("This is not a list\n");
		exit(1);
	}

	len = (int) PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int) ((PyListObject *) p)->allocated);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: %s\n",
		       i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
