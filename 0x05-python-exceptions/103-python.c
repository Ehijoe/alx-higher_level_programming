#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <bytesobject.h>
#include <object.h>
#include <listobject.h>
#include <floatobject.h>

#include <stdio.h>
#include <stdlib.h>


/**
 * print_python_float - Print a python float object
 * @p: Pointer to the float object
 */
void print_python_float(PyObject *p)
{
	char repr[100] = {};
	int i;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	sprintf(repr, "%1.15f", (double)((PyFloatObject *) p)->ob_fval);
	for (i = 99; i > 0; i++)
	{
		if (repr[i] != '0')
			break;
		repr[i] = '\0';
	}
	printf("  value: %s\n", repr);
}


/**
 * print_python_bytes - Print a python bytes object
 * @p: Pointer to the bytes object
 */
void print_python_bytes(PyObject *p)
{
	int size, i;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *) p)->ob_size;
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *) p)->ob_sval);
	size = (size >= 10) ? 10 : size + 1;
	printf("  first %d bytes:", size);
	for (i = 0; i < size; i++)
	{
		printf(" %02x", 0xff & ((PyBytesObject *) p)->ob_sval[i]);
	}
	printf("\n");
}


/**
 * print_python_list - Prints information about a python list
 * @p: A pointer to the list object
 */
void print_python_list(PyObject *p)
{
	int len, i;
	PyObject *item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		exit(1);
	}

	len = (int) ((PyVarObject *) p)->ob_size;
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int) ((PyListObject *) p)->allocated);

	for (i = 0; i < len; i++)
	{
		item = ((PyListObject *) p)->ob_item[i];
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
		if (strcmp(item->ob_type->tp_name, "float") == 0)
			print_python_float(item);
	}
}
